const {
  Client,
  GatewayIntentBits,
  PermissionFlagsBits,
  ChannelType,
  SlashCommandBuilder,
  REST,
  Routes,
} = require("discord.js");
const express = require("express");
require("dotenv").config();

// Get bot token with fallback
const BOT_TOKEN = process.env.DISCORD_TOKEN || process.env.DISCORD_BOT_TOKEN;
const CLIENT_ID = process.env.CLIENT_ID;
const GUILD_ID = process.env.GUILD_ID;

// Debug logging for environment variables
console.log("🔍 Environment Variables Debug:");
console.log("DISCORD_TOKEN exists:", !!process.env.DISCORD_TOKEN);
console.log("DISCORD_BOT_TOKEN exists:", !!process.env.DISCORD_BOT_TOKEN);
console.log("CLIENT_ID exists:", !!process.env.CLIENT_ID);
console.log("GUILD_ID exists:", !!process.env.GUILD_ID);
console.log("PORT:", process.env.PORT);
if (BOT_TOKEN) {
  console.log("Token length:", BOT_TOKEN.length);
  console.log("Token starts with:", BOT_TOKEN.substring(0, 10) + "...");
} else {
  console.error("❌ No bot token found in DISCORD_TOKEN or DISCORD_BOT_TOKEN");
}

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
    GatewayIntentBits.GuildMembers,
  ],
});

// Express server for Railway health checks
const app = express();
const port = process.env.PORT || 3000;

// Health check endpoint
app.get("/health", (req, res) => {
  res.json({
    status: "healthy",
    uptime: process.uptime(),
    timestamp: new Date().toISOString(),
    bot_status: client.isReady() ? "connected" : "disconnected",
  });
});

// Keep Railway from sleeping
app.get("/", (req, res) => {
  res.send("Discord Invisible Bot is running! 👻");
});

app
  .listen(port, "0.0.0.0", () => {
    console.log(`Health check server running on port ${port}`);
  })
  .on("error", (err) => {
    console.error("Health server error:", err);
  });

// Slash commands
const commands = [
  new SlashCommandBuilder()
    .setName("create-invisible-role")
    .setDescription("Create an invisible role")
    .addStringOption((option) =>
      option
        .setName("name")
        .setDescription("Name of the invisible role")
        .setRequired(true),
    )
    .addStringOption((option) =>
      option
        .setName("color")
        .setDescription("Hex color code for the role (e.g., #ff0000)")
        .setRequired(false),
    ),

  new SlashCommandBuilder()
    .setName("create-invisible-room")
    .setDescription("Create an invisible room (channel)")
    .addStringOption((option) =>
      option
        .setName("name")
        .setDescription("Name of the invisible channel")
        .setRequired(true),
    )
    .addRoleOption((option) =>
      option
        .setName("role")
        .setDescription("Role that can access the invisible channel")
        .setRequired(true),
    )
    .addStringOption((option) =>
      option
        .setName("type")
        .setDescription("Channel type")
        .setRequired(false)
        .addChoices(
          { name: "Text Channel", value: "text" },
          { name: "Voice Channel", value: "voice" },
        ),
    ),

  new SlashCommandBuilder()
    .setName("assign-invisible-role")
    .setDescription("Assign invisible role to a user")
    .addUserOption((option) =>
      option
        .setName("user")
        .setDescription("User to assign the role to")
        .setRequired(true),
    )
    .addRoleOption((option) =>
      option
        .setName("role")
        .setDescription("Invisible role to assign")
        .setRequired(true),
    ),

  new SlashCommandBuilder()
    .setName("list-invisible")
    .setDescription("List all invisible roles and channels"),
];

client.once("ready", async () => {
  console.log(`Logged in as ${client.user.tag}!`);

  // Register slash commands
  const rest = new REST({ version: "10" }).setToken(BOT_TOKEN);

  try {
    console.log("Started refreshing application (/) commands.");

    await rest.put(Routes.applicationGuildCommands(CLIENT_ID, GUILD_ID), {
      body: commands,
    });

    console.log("Successfully reloaded application (/) commands.");
  } catch (error) {
    console.error(error);
  }
});

client.on("interactionCreate", async (interaction) => {
  if (!interaction.isChatInputCommand()) return;

  const { commandName } = interaction;

  // Check if user has administrator permissions
  if (!interaction.member.permissions.has(PermissionFlagsBits.Administrator)) {
    await interaction.reply({
      content: "❌ You need Administrator permissions to use this command.",
      ephemeral: true,
    });
    return;
  }

  try {
    switch (commandName) {
      case "create-invisible-role":
        await handleCreateInvisibleRole(interaction);
        break;
      case "create-invisible-room":
        await handleCreateInvisibleRoom(interaction);
        break;
      case "assign-invisible-role":
        await handleAssignInvisibleRole(interaction);
        break;
      case "list-invisible":
        await handleListInvisible(interaction);
        break;
    }
  } catch (error) {
    console.error("Error handling command:", error);
    const errorMessage = "❌ An error occurred while executing the command.";

    if (interaction.replied || interaction.deferred) {
      await interaction.followUp({ content: errorMessage, ephemeral: true });
    } else {
      await interaction.reply({ content: errorMessage, ephemeral: true });
    }
  }
});

async function handleCreateInvisibleRole(interaction) {
  const roleName = interaction.options.getString("name");
  const colorHex = interaction.options.getString("color");

  let color = null;
  if (colorHex) {
    // Validate hex color
    if (!/^#[0-9A-F]{6}$/i.test(colorHex)) {
      await interaction.reply({
        content: "❌ Invalid color format. Please use hex format like #ff0000",
        ephemeral: true,
      });
      return;
    }
    color = colorHex;
  }

  const role = await interaction.guild.roles.create({
    name: roleName,
    color: color,
    hoist: false, // Don't display separately in member list (invisible)
    mentionable: false, // Can't be mentioned by regular users
    permissions: [], // No special permissions by default
    reason: `Invisible role created by ${interaction.user.tag}`,
  });

  await interaction.reply({
    content:
      `✅ Created invisible role: **${role.name}**\n` +
      `📋 Role ID: \`${role.id}\`\n` +
      `🎨 Color: ${color || "Default"}\n` +
      `👻 This role is invisible (not hoisted) and non-mentionable.`,
    ephemeral: true,
  });
}

async function handleCreateInvisibleRoom(interaction) {
  const channelName = interaction.options.getString("name");
  const allowedRole = interaction.options.getRole("role");
  const channelType = interaction.options.getString("type") || "text";

  const channelOptions = {
    name: channelName,
    type:
      channelType === "voice" ? ChannelType.GuildVoice : ChannelType.GuildText,
    permissionOverwrites: [
      {
        id: interaction.guild.id, // @everyone role
        deny: [
          PermissionFlagsBits.ViewChannel,
          PermissionFlagsBits.SendMessages,
          PermissionFlagsBits.Connect,
        ],
      },
      {
        id: allowedRole.id, // Specified role
        allow: [
          PermissionFlagsBits.ViewChannel,
          PermissionFlagsBits.SendMessages,
          PermissionFlagsBits.ReadMessageHistory,
          ...(channelType === "voice"
            ? [PermissionFlagsBits.Connect, PermissionFlagsBits.Speak]
            : []),
        ],
      },
    ],
    reason: `Invisible ${channelType} channel created by ${interaction.user.tag}`,
  };

  const channel = await interaction.guild.channels.create(channelOptions);

  await interaction.reply({
    content:
      `✅ Created invisible ${channelType} channel: ${channel}\n` +
      `📋 Channel ID: \`${channel.id}\`\n` +
      `🔒 Only users with the **${allowedRole.name}** role can see and access this channel.\n` +
      `👻 This channel is invisible to everyone else.`,
    ephemeral: true,
  });
}

async function handleAssignInvisibleRole(interaction) {
  const user = interaction.options.getUser("user");
  const role = interaction.options.getRole("role");

  const member = await interaction.guild.members.fetch(user.id);

  if (member.roles.cache.has(role.id)) {
    await interaction.reply({
      content: `❌ ${user.tag} already has the **${role.name}** role.`,
      ephemeral: true,
    });
    return;
  }

  await member.roles.add(
    role,
    `Invisible role assigned by ${interaction.user.tag}`,
  );

  await interaction.reply({
    content:
      `✅ Successfully assigned the **${role.name}** role to ${user.tag}\n` +
      `👻 This role is invisible and won't show in the member list.`,
    ephemeral: true,
  });
}

async function handleListInvisible(interaction) {
  const guild = interaction.guild;

  // Find invisible roles (not hoisted and created by bot or matching criteria)
  const invisibleRoles = guild.roles.cache.filter(
    (role) =>
      !role.hoist &&
      role.id !== guild.id && // Exclude @everyone
      !role.managed && // Exclude bot roles
      !role.permissions.has(PermissionFlagsBits.Administrator),
  );

  // Find channels with restricted permissions (likely invisible)
  const invisibleChannels = guild.channels.cache.filter((channel) => {
    if (
      channel.type !== ChannelType.GuildText &&
      channel.type !== ChannelType.GuildVoice
    )
      return false;

    const everyoneOverwrite = channel.permissionOverwrites.cache.get(guild.id);
    return (
      everyoneOverwrite &&
      everyoneOverwrite.deny.has(PermissionFlagsBits.ViewChannel)
    );
  });

  let response = "## 👻 Invisible Elements\n\n";

  if (invisibleRoles.size > 0) {
    response += "### 🎭 Invisible Roles:\n";
    invisibleRoles.forEach((role) => {
      const memberCount = role.members.size;
      response += `• **${role.name}** (${memberCount} member${memberCount !== 1 ? "s" : ""})\n`;
      response += `  📋 ID: \`${role.id}\`\n`;
    });
    response += "\n";
  } else {
    response += "### 🎭 Invisible Roles:\n*No invisible roles found.*\n\n";
  }

  if (invisibleChannels.size > 0) {
    response += "### 🔒 Invisible Channels:\n";
    invisibleChannels.forEach((channel) => {
      const type = channel.type === ChannelType.GuildVoice ? "🔊" : "💬";
      response += `• ${type} **${channel.name}**\n`;
      response += `  📋 ID: \`${channel.id}\`\n`;
    });
  } else {
    response += "### 🔒 Invisible Channels:\n*No invisible channels found.*\n";
  }

  await interaction.reply({
    content: response,
    ephemeral: true,
  });
}

// Error handling
client.on("error", (error) => {
  console.error("Discord client error:", error);
});

process.on("unhandledRejection", (error) => {
  console.error("Unhandled promise rejection:", error);
});

// Graceful shutdown
process.on("SIGINT", () => {
  console.log("Received SIGINT, shutting down gracefully...");
  client.destroy();
  process.exit(0);
});

process.on("SIGTERM", () => {
  console.log("Received SIGTERM, shutting down gracefully...");
  client.destroy();
  process.exit(0);
});

// Login to Discord
console.log("🚀 Attempting to login with token...");
if (!BOT_TOKEN) {
  console.error(
    "❌ No bot token found! Set DISCORD_TOKEN or DISCORD_BOT_TOKEN",
  );
  // Don't exit - keep health server running
  console.log("⚠️ Bot login failed, but health server continues...");
} else if (!CLIENT_ID || !GUILD_ID) {
  console.error("❌ Missing CLIENT_ID or GUILD_ID environment variables!");
  console.log("⚠️ Bot login failed, but health server continues...");
} else {
  client.login(BOT_TOKEN).catch((err) => {
    console.error("❌ Bot login failed:", err);
    console.log("⚠️ Bot login failed, but health server continues...");
  });
}

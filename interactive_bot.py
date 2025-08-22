#!/usr/bin/env python3
"""
Interactive Discord Bot
A simple bot that responds to commands and demonstrates basic functionality.
"""

import discord
from discord.ext import commands
import asyncio
import os
import sys
from datetime import datetime

# Bot configuration
BOT_TOKEN = ""
COMMAND_PREFIX = "!"

# Setup intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# Create bot instance
bot = commands.Bot(
    command_prefix=COMMAND_PREFIX,
    intents=intents,
    help_command=commands.DefaultHelpCommand()
)

@bot.event
async def on_ready():
    """Bot startup event"""
    print("\n" + "="*50)
    print("🤖 BOT IS NOW ONLINE!")
    print("="*50)
    print(f"Bot Name: {bot.user.name}#{bot.user.discriminator}")
    print(f"Bot ID: {bot.user.id}")
    print(f"Connected to {len(bot.guilds)} servers")
    print(f"Command Prefix: {COMMAND_PREFIX}")
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    if bot.guilds:
        print("\n📋 Server List:")
        for guild in bot.guilds:
            print(f"  • {guild.name} ({guild.member_count} members)")

    print("\n💡 Available Commands:")
    print(f"  {COMMAND_PREFIX}ping - Check bot latency")
    print(f"  {COMMAND_PREFIX}status - Bot status report")
    print(f"  {COMMAND_PREFIX}hello - Simple greeting")
    print(f"  {COMMAND_PREFIX}server - Server information")
    print(f"  {COMMAND_PREFIX}user - User information")
    print(f"  {COMMAND_PREFIX}help - Show all commands")
    print("\n🎯 Bot is ready for commands!")
    print("="*50)

@bot.event
async def on_message(message):
    """Handle incoming messages"""
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Log messages (optional - for debugging)
    if message.content.startswith(COMMAND_PREFIX):
        print(f"📝 Command: {message.content} from {message.author} in #{message.channel}")

    # Process commands
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    """Handle command errors"""
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"❌ Unknown command. Type `{COMMAND_PREFIX}help` for available commands.")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ You don't have permission to use this command.")
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send("❌ I don't have permission to perform this action.")
    else:
        print(f"❌ Command error: {error}")
        await ctx.send(f"❌ An error occurred: {str(error)}")

# Basic Commands
@bot.command(name='ping')
async def ping(ctx):
    """Check bot latency"""
    latency = round(bot.latency * 1000, 1)

    embed = discord.Embed(
        title="🏓 Pong!",
        color=discord.Color.green(),
        timestamp=datetime.utcnow()
    )
    embed.add_field(name="Latency", value=f"{latency}ms", inline=True)
    embed.add_field(name="Status", value="✅ Online", inline=True)

    await ctx.send(embed=embed)

@bot.command(name='hello', aliases=['hi', 'hey'])
async def hello(ctx):
    """Simple greeting command"""
    greetings = [
        f"Hello {ctx.author.mention}! 👋",
        f"Hey there, {ctx.author.display_name}! 😊",
        f"Hi {ctx.author.mention}! How can I help you today? 🤖",
        f"Greetings, {ctx.author.display_name}! 🎉"
    ]

    import random
    greeting = random.choice(greetings)

    embed = discord.Embed(
        title="👋 Greetings!",
        description=greeting,
        color=discord.Color.blue()
    )

    await ctx.send(embed=embed)

@bot.command(name='status')
async def status(ctx):
    """Comprehensive bot status"""
    uptime = datetime.utcnow() - bot.uptime if hasattr(bot, 'uptime') else None

    embed = discord.Embed(
        title="🤖 Bot Status",
        color=discord.Color.green(),
        timestamp=datetime.utcnow()
    )

    embed.add_field(
        name="📊 Connection",
        value=f"✅ Online\n📡 {round(bot.latency * 1000, 1)}ms",
        inline=True
    )

    embed.add_field(
        name="🏠 Servers",
        value=f"🎯 This Server: {ctx.guild.name}\n📈 Total: {len(bot.guilds)}",
        inline=True
    )

    embed.add_field(
        name="👥 Users",
        value=f"👤 This Server: {ctx.guild.member_count}\n🌍 Total: {sum(g.member_count for g in bot.guilds)}",
        inline=True
    )

    embed.set_footer(text=f"Bot ID: {bot.user.id}")

    await ctx.send(embed=embed)

@bot.command(name='server', aliases=['serverinfo'])
async def server_info(ctx):
    """Display server information"""
    guild = ctx.guild

    embed = discord.Embed(
        title=f"🏠 {guild.name}",
        color=discord.Color.blue(),
        timestamp=datetime.utcnow()
    )

    if guild.icon:
        embed.set_thumbnail(url=guild.icon.url)

    embed.add_field(name="👑 Owner", value=guild.owner.mention, inline=True)
    embed.add_field(name="👥 Members", value=guild.member_count, inline=True)
    embed.add_field(name="💬 Channels", value=len(guild.channels), inline=True)
    embed.add_field(name="🎭 Roles", value=len(guild.roles), inline=True)
    embed.add_field(name="📅 Created", value=guild.created_at.strftime("%B %d, %Y"), inline=True)
    embed.add_field(name="🆔 Server ID", value=guild.id, inline=True)

    await ctx.send(embed=embed)

@bot.command(name='user', aliases=['userinfo', 'whois'])
async def user_info(ctx, member: discord.Member = None):
    """Display user information"""
    member = member or ctx.author

    embed = discord.Embed(
        title=f"👤 {member.display_name}",
        color=member.color if member.color != discord.Color.default() else discord.Color.blue(),
        timestamp=datetime.utcnow()
    )

    embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)

    embed.add_field(name="📛 Username", value=f"{member.name}#{member.discriminator}", inline=True)
    embed.add_field(name="🆔 User ID", value=member.id, inline=True)
    embed.add_field(name="📅 Joined Discord", value=member.created_at.strftime("%B %d, %Y"), inline=True)
    embed.add_field(name="📅 Joined Server", value=member.joined_at.strftime("%B %d, %Y"), inline=True)
    embed.add_field(name="🎭 Roles", value=len(member.roles) - 1, inline=True)  # -1 to exclude @everyone
    embed.add_field(name="🤖 Bot", value="Yes" if member.bot else "No", inline=True)

    if member.roles[1:]:  # Exclude @everyone role
        roles = ", ".join([role.mention for role in member.roles[1:]])
        embed.add_field(name="🏷️ Role List", value=roles[:1024], inline=False)  # Discord field limit

    await ctx.send(embed=embed)

@bot.command(name='echo')
async def echo(ctx, *, message=None):
    """Echo back a message"""
    if not message:
        await ctx.send("❌ Please provide a message to echo!")
        return

    embed = discord.Embed(
        title="📢 Echo",
        description=message,
        color=discord.Color.purple()
    )
    embed.set_footer(text=f"Requested by {ctx.author.display_name}")

    await ctx.send(embed=embed)

@bot.command(name='uptime')
async def uptime(ctx):
    """Show bot uptime"""
    if hasattr(bot, 'start_time'):
        uptime = datetime.utcnow() - bot.start_time
        days = uptime.days
        hours, remainder = divmod(uptime.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        uptime_str = f"{days}d {hours}h {minutes}m {seconds}s"
    else:
        uptime_str = "Unknown"

    embed = discord.Embed(
        title="⏱️ Bot Uptime",
        description=f"I've been online for: **{uptime_str}**",
        color=discord.Color.green()
    )

    await ctx.send(embed=embed)

# Fun Commands
@bot.command(name='roll')
async def roll_dice(ctx, sides: int = 6):
    """Roll a dice (default 6 sides)"""
    import random

    if sides < 2 or sides > 100:
        await ctx.send("❌ Dice must have between 2 and 100 sides!")
        return

    result = random.randint(1, sides)

    embed = discord.Embed(
        title="🎲 Dice Roll",
        description=f"You rolled a **{result}** on a {sides}-sided dice!",
        color=discord.Color.gold()
    )

    await ctx.send(embed=embed)

@bot.command(name='flip')
async def flip_coin(ctx):
    """Flip a coin"""
    import random

    result = random.choice(["Heads", "Tails"])
    emoji = "🪙" if result == "Heads" else "🪙"

    embed = discord.Embed(
        title=f"{emoji} Coin Flip",
        description=f"The coin landed on: **{result}**!",
        color=discord.Color.gold()
    )

    await ctx.send(embed=embed)

# Admin Commands (if bot has permissions)
@bot.command(name='clean', aliases=['purge'])
@commands.has_permissions(manage_messages=True)
async def clean_messages(ctx, amount: int = 5):
    """Clean recent messages (requires Manage Messages permission)"""
    if amount < 1 or amount > 100:
        await ctx.send("❌ Amount must be between 1 and 100!")
        return

    deleted = await ctx.channel.purge(limit=amount + 1)  # +1 to include command message

    embed = discord.Embed(
        title="🧹 Messages Cleaned",
        description=f"Deleted {len(deleted) - 1} messages.",
        color=discord.Color.green()
    )

    # Send confirmation message that auto-deletes
    msg = await ctx.send(embed=embed)
    await asyncio.sleep(3)
    await msg.delete()

# Error handler for permission errors
@clean_messages.error
async def clean_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ I need 'Manage Messages' permission to clean messages!")

def main():
    """Main function to run the bot"""
    print("🚀 Starting Discord Bot...")
    print("Press Ctrl+C to stop the bot")

    # Store start time for uptime command
    bot.start_time = datetime.utcnow()

    try:
        bot.run(BOT_TOKEN)
    except discord.LoginFailure:
        print("❌ Invalid bot token! Check your token in the script.")
    except KeyboardInterrupt:
        print("\n🛑 Bot stopped by user")
    except Exception as e:
        print(f"❌ Bot error: {e}")

if __name__ == "__main__":
    main()

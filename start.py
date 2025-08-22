#!/usr/bin/env python3
"""
Railway Deployment Startup Script for Discord Bot
Automatically starts the bot when deployed to Railway.
"""

import os
import sys
import logging
from datetime import datetime
import discord
from discord.ext import commands

# Configure logging for Railway
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

# Bot configuration
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
COMMAND_PREFIX = os.getenv('COMMAND_PREFIX', '!')
ENVIRONMENT = os.getenv('RAILWAY_ENVIRONMENT', 'development')

if not BOT_TOKEN:
    logger.error("DISCORD_BOT_TOKEN environment variable not found!")
    logger.error("Please set your Discord bot token in Railway environment variables.")
    sys.exit(1)

# Setup intents
intents = discord.Intents.default()
intents.message_content = True  # Required for reading message content
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
    logger.info("="*50)
    logger.info("🤖 DISCORD BOT DEPLOYED ON RAILWAY!")
    logger.info("="*50)
    logger.info(f"Bot Name: {bot.user.name}#{bot.user.discriminator}")
    logger.info(f"Bot ID: {bot.user.id}")
    logger.info(f"Connected to {len(bot.guilds)} servers")
    logger.info(f"Command Prefix: {COMMAND_PREFIX}")
    logger.info(f"Environment: {ENVIRONMENT}")
    logger.info(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    if bot.guilds:
        logger.info("📋 Server List:")
        for guild in bot.guilds:
            logger.info(f"  • {guild.name} ({guild.member_count} members)")

    logger.info("🎯 Bot is ready for commands!")
    logger.info("="*50)

    # Set bot status
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"{len(bot.guilds)} servers | {COMMAND_PREFIX}help"
        )
    )

@bot.event
async def on_guild_join(guild):
    """Bot joins a new server"""
    logger.info(f"🎉 Joined new server: {guild.name} ({guild.member_count} members)")

    # Update presence
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"{len(bot.guilds)} servers | {COMMAND_PREFIX}help"
        )
    )

@bot.event
async def on_guild_remove(guild):
    """Bot leaves a server"""
    logger.info(f"👋 Left server: {guild.name}")

    # Update presence
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=f"{len(bot.guilds)} servers | {COMMAND_PREFIX}help"
        )
    )

@bot.event
async def on_message(message):
    """Handle incoming messages"""
    if message.author == bot.user:
        return

    # Log commands for debugging
    if message.content.startswith(COMMAND_PREFIX):
        logger.info(f"📝 Command: {message.content} from {message.author} in #{message.channel} ({message.guild.name})")

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
        logger.error(f"Command error: {error}")
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
    embed.add_field(name="Status", value="✅ Online (Railway)", inline=True)
    embed.add_field(name="Environment", value=ENVIRONMENT, inline=True)

    await ctx.send(embed=embed)

@bot.command(name='hello', aliases=['hi', 'hey'])
async def hello(ctx):
    """Simple greeting command"""
    greetings = [
        f"Hello {ctx.author.mention}! 👋 I'm running on Railway!",
        f"Hey there, {ctx.author.display_name}! 😊 Deployed and ready!",
        f"Hi {ctx.author.mention}! How can I help you today? 🚂",
        f"Greetings, {ctx.author.display_name}! 🎉 Live from Railway!"
    ]

    import random
    greeting = random.choice(greetings)

    embed = discord.Embed(
        title="👋 Greetings from Railway!",
        description=greeting,
        color=discord.Color.blue()
    )

    await ctx.send(embed=embed)

@bot.command(name='status')
async def status(ctx):
    """Comprehensive bot status"""
    embed = discord.Embed(
        title="🤖 Bot Status (Railway Deployment)",
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
        name="🚂 Platform",
        value=f"Railway\nEnv: {ENVIRONMENT}",
        inline=True
    )

    embed.add_field(
        name="👥 Users",
        value=f"👤 This Server: {ctx.guild.member_count}\n🌍 Total: {sum(g.member_count for g in bot.guilds)}",
        inline=True
    )

    embed.set_footer(text=f"Bot ID: {bot.user.id} • Deployed on Railway")

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

@bot.command(name='railway')
async def railway_info(ctx):
    """Display Railway deployment information"""
    embed = discord.Embed(
        title="🚂 Railway Deployment Info",
        color=discord.Color.purple(),
        timestamp=datetime.utcnow()
    )

    embed.add_field(name="🌍 Environment", value=ENVIRONMENT, inline=True)
    embed.add_field(name="🔧 Platform", value="Railway", inline=True)
    embed.add_field(name="⚡ Status", value="✅ Running", inline=True)

    # Add Railway-specific environment info if available
    railway_env = os.getenv('RAILWAY_ENVIRONMENT_NAME', 'production')
    railway_service = os.getenv('RAILWAY_SERVICE_NAME', 'discord-bot')

    embed.add_field(name="🏷️ Service", value=railway_service, inline=True)
    embed.add_field(name="🎯 Environment", value=railway_env, inline=True)
    embed.add_field(name="🕒 Uptime", value="Since last deployment", inline=True)

    embed.set_footer(text="Powered by Railway.app")

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

    embed = discord.Embed(
        title="🪙 Coin Flip",
        description=f"The coin landed on: **{result}**!",
        color=discord.Color.gold()
    )

    await ctx.send(embed=embed)

def main():
    """Main function to run the bot"""
    logger.info("🚀 Starting Discord Bot on Railway...")
    logger.info("Environment: " + ENVIRONMENT)

    try:
        # Run the bot
        bot.run(BOT_TOKEN)
    except discord.LoginFailure:
        logger.error("❌ Invalid bot token! Check DISCORD_BOT_TOKEN environment variable.")
        sys.exit(1)
    except KeyboardInterrupt:
        logger.info("🛑 Bot stopped by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"❌ Bot error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

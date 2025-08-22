#!/usr/bin/env python3
"""
Minimal Discord Bot Status Checker
Simple script to test if your Discord bot is online and working.
"""

import discord
import asyncio
import os
import sys
import warnings
from datetime import datetime
from dotenv import load_dotenv

# Suppress aiohttp warnings
warnings.filterwarnings("ignore", message=".*Unclosed.*")
warnings.filterwarnings("ignore", category=ResourceWarning)

class MinimalBotChecker:
    def __init__(self, token):
        self.token = token
        self.results = {
            'connected': False,
            'bot_info': None,
            'guilds': [],
            'latency': None,
            'error': None
        }

    async def check_status(self):
        """Quick status check with automatic cleanup"""
        print("🔍 Checking Discord bot status...")

        # Create minimal client
        intents = discord.Intents.default()
        client = discord.Client(intents=intents)

        @client.event
        async def on_ready():
            try:
                # Gather information
                self.results['connected'] = True
                self.results['bot_info'] = {
                    'name': client.user.name,
                    'id': client.user.id,
                    'discriminator': client.user.discriminator
                }
                self.results['latency'] = round(client.latency * 1000, 1)
                self.results['guilds'] = [
                    {'name': guild.name, 'id': guild.id, 'members': guild.member_count}
                    for guild in client.guilds
                ]

                # Print results immediately
                self.print_results()

            except Exception as e:
                self.results['error'] = str(e)
                print(f"❌ Error gathering info: {e}")

            finally:
                # Close connection quickly
                await client.close()

        try:
            # Connect with timeout
            await asyncio.wait_for(client.start(self.token), timeout=8.0)

        except asyncio.TimeoutError:
            self.results['error'] = "Connection timeout"
            print("❌ Connection timeout (8 seconds)")

        except discord.LoginFailure:
            self.results['error'] = "Invalid token"
            print("❌ Authentication failed - Check your bot token")

        except Exception as e:
            self.results['error'] = str(e)
            print(f"❌ Connection error: {e}")

        finally:
            if not client.is_closed():
                await client.close()
            # Brief pause for cleanup
            await asyncio.sleep(0.1)

    def print_results(self):
        """Print formatted results"""
        print("\n" + "="*50)
        print("📊 BOT STATUS REPORT")
        print("="*50)

        if self.results['connected']:
            bot = self.results['bot_info']
            print(f"✅ Status: ONLINE")
            print(f"🤖 Bot: {bot['name']}#{bot['discriminator']}")
            print(f"🆔 ID: {bot['id']}")
            print(f"📡 Latency: {self.results['latency']}ms")
            print(f"🏠 Servers: {len(self.results['guilds'])}")

            if self.results['guilds']:
                print("\n📋 Server List:")
                for guild in self.results['guilds'][:10]:  # Show max 10
                    print(f"  • {guild['name']} ({guild['members']} members)")
                if len(self.results['guilds']) > 10:
                    print(f"  ... and {len(self.results['guilds']) - 10} more servers")
            else:
                print("\n⚠️  Bot is not in any servers yet")
                print("💡 Add bot to server via Discord Developer Portal > OAuth2")

        else:
            print(f"❌ Status: OFFLINE")
            if self.results['error']:
                print(f"🔥 Error: {self.results['error']}")

        print(f"\n⏰ Check time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*50)

def get_bot_token():
    """Get bot token from environment or user input"""
    # Load environment variables from .env file
    load_dotenv()

    # Try environment variable first
    token = os.getenv('DISCORD_TOKEN')
    if token:
        print("🔑 Using token from DISCORD_TOKEN environment variable")
        return token

    # Try command line argument
    if len(sys.argv) > 1:
        token = sys.argv[1]
        print("🔑 Using token from command line argument")
        return token

    # Ask user for token
    print("🔑 No token found in environment variable DISCORD_TOKEN")
    print("💡 You can set it with: export DISCORD_TOKEN=your_token_here")
    print("💡 Or create a .env file with: DISCORD_TOKEN=your_token_here")
    print("📝 Or pass it as argument: python3 status_check.py YOUR_TOKEN")

    token = input("\nEnter your Discord bot token: ").strip()
    if not token:
        print("❌ No token provided!")
        return None

    return token

async def main():
    """Main function"""
    print("🤖 Discord Bot Status Checker")
    print("=" * 50)

    # Get token
    token = get_bot_token()
    if not token:
        sys.exit(1)

    # Run check
    checker = MinimalBotChecker(token)

    try:
        await checker.check_status()

        # Show help if not connected
        if not checker.results['connected']:
            print("\n🆘 Troubleshooting:")
            print("  1. Verify bot token is correct")
            print("  2. Check Discord Developer Portal settings")
            print("  3. Ensure bot has proper permissions")
            print("  4. Try regenerating bot token if needed")

    except KeyboardInterrupt:
        print("\n🛑 Check cancelled by user")

    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"💥 Fatal error: {e}")
        sys.exit(1)

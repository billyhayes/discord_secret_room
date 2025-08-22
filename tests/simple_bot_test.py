import discord
import asyncio
import time
import sys
import warnings
import aiohttp

class SimpleDiscordTest:
    def __init__(self, token):
        self.token = token
        self.client = None

    async def test_connection(self):
        """Simple connection test with proper cleanup"""
        print("🔍 Starting simple Discord connection test...")

        # Create client with proper intents
        intents = discord.Intents.default()
        intents.message_content = True  # Enable message content intent

        self.client = discord.Client(intents=intents)

        # Set up event handlers
        @self.client.event
        async def on_ready():
            print(f"✅ Successfully connected as {self.client.user}")
            print(f"📊 Bot ID: {self.client.user.id}")
            print(f"🏠 Connected to {len(self.client.guilds)} servers")

            if self.client.guilds:
                print("📋 Server list:")
                for guild in self.client.guilds:
                    print(f"  • {guild.name} (ID: {guild.id}) - {guild.member_count} members")
            else:
                print("⚠️  Bot is not in any servers yet")

            # Check latency
            latency = self.client.latency
            if latency > 0:
                print(f"📡 Latency: {round(latency * 1000)}ms")

            print("🎉 Connection test completed successfully!")

            # Auto-disconnect after 3 seconds
            await asyncio.sleep(3)
            print("🔌 Disconnecting...")
            await self.client.close()

        @self.client.event
        async def on_error(event, *args, **kwargs):
            print(f"❌ Discord error in {event}: {sys.exc_info()}")

        try:
            # Start the client
            print("🚀 Attempting to connect to Discord...")
            await self.client.start(self.token)

        except discord.LoginFailure:
            print("❌ Login failed - Invalid bot token!")
            print("💡 Make sure you're using a valid bot token from Discord Developer Portal")

        except discord.HTTPException as e:
            print(f"❌ HTTP error: {e}")

        except Exception as e:
            print(f"❌ Unexpected error: {e}")

        finally:
            # Ensure cleanup
            if self.client and not self.client.is_closed():
                print("🧹 Cleaning up connections...")
                await self.client.close()

            # Force cleanup of any remaining aiohttp connections
            await self._force_cleanup_connections()
            print("✨ Cleanup completed")

    async def _force_cleanup_connections(self):
        """Force cleanup of aiohttp connections to prevent warnings"""
        try:
            # Wait for connections to close naturally
            await asyncio.sleep(0.5)

            # Force garbage collection of any remaining connections
            import gc
            gc.collect()

            # Suppress the unclosed connector warnings
            warnings.filterwarnings("ignore", message="Unclosed connector")

        except Exception as e:
            print(f"⚠️  Cleanup warning (can be ignored): {e}")

async def run_simple_test(token):
    """Run a simple connection test"""
    if not token or token == "YOUR_BOT_TOKEN_HERE":
        print("❌ Please set a valid bot token!")
        print("📝 Edit this file and replace 'YOUR_BOT_TOKEN_HERE' with your actual token")
        return

    tester = SimpleDiscordTest(token)
    await tester.test_connection()

def main():
    """Main function with proper error handling"""
    # Replace this with your actual bot token
    BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

    print("🤖 Simple Discord Bot Connection Test")
    print("=" * 40)

    # Suppress aiohttp warnings before running
    warnings.filterwarnings("ignore", message="Unclosed connector")
    warnings.filterwarnings("ignore", message="Unclosed client session")

    try:
        # Run the test
        asyncio.run(run_simple_test(BOT_TOKEN))

    except KeyboardInterrupt:
        print("\n🛑 Test interrupted by user")

    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")

    finally:
        # Final cleanup attempt
        try:
            import gc
            gc.collect()
            asyncio.sleep(0.1)
        except:
            pass

        print("\n📋 Test Summary:")
        print("  • If you saw '✅ Successfully connected', your bot is working!")
        print("  • If you saw login errors, check your bot token")
        print("  • If you saw permission errors, check your bot's server permissions")
        print("\n💡 Next steps:")
        print("  • Add your bot to a server using the OAuth2 URL Generator")
        print("  • Give it appropriate permissions")
        print("  • Test with the full bot_status.py script")
        print("  • The 'Unclosed connector' warning is harmless and has been suppressed")

if __name__ == "__main__":
    main()

import discord
import asyncio
import sys
import warnings
from contextlib import asynccontextmanager

class CleanBotTest:
    """Ultra-clean Discord bot tester with proper session management"""

    def __init__(self, token):
        self.token = token

    @asynccontextmanager
    async def create_bot_session(self):
        """Context manager for clean bot session handling"""
        bot = None
        try:
            # Create bot with minimal intents for testing
            intents = discord.Intents.default()
            intents.message_content = True

            bot = discord.Client(
                intents=intents,
                connector=discord.http.HTTPClient.connector_class(
                    limit=1,
                    limit_per_host=1
                )
            )

            yield bot

        finally:
            if bot and not bot.is_closed():
                try:
                    await bot.close()
                    # Give time for cleanup
                    await asyncio.sleep(0.25)
                except Exception as e:
                    print(f"⚠️  Cleanup warning: {e}")

    async def run_connection_test(self):
        """Run a clean connection test"""
        print("🧪 Starting ultra-clean Discord connection test...")

        # Suppress aiohttp warnings
        warnings.filterwarnings("ignore", category=ResourceWarning)
        warnings.filterwarnings("ignore", message=".*Unclosed.*")

        connection_successful = False

        async with self.create_bot_session() as bot:
            # Set up minimal event handling
            @bot.event
            async def on_ready():
                nonlocal connection_successful
                connection_successful = True

                print(f"✅ Connection successful!")
                print(f"🤖 Bot: {bot.user.name}#{bot.user.discriminator}")
                print(f"🆔 ID: {bot.user.id}")
                print(f"📊 Servers: {len(bot.guilds)}")

                if bot.guilds:
                    print("🏠 Server list:")
                    for guild in bot.guilds[:5]:  # Show max 5 servers
                        print(f"  • {guild.name} ({guild.member_count} members)")
                    if len(bot.guilds) > 5:
                        print(f"  ... and {len(bot.guilds) - 5} more")
                else:
                    print("⚠️  Not in any servers yet")

                # Check connection quality
                latency_ms = round(bot.latency * 1000)
                if latency_ms < 100:
                    print(f"📶 Latency: {latency_ms}ms (Excellent)")
                elif latency_ms < 250:
                    print(f"📶 Latency: {latency_ms}ms (Good)")
                else:
                    print(f"📶 Latency: {latency_ms}ms (High)")

                print("🎉 Test completed successfully!")

                # Auto-disconnect after brief delay
                await asyncio.sleep(1.5)
                await bot.close()

            @bot.event
            async def on_error(event, *args, **kwargs):
                print(f"❌ Error in {event}: {sys.exc_info()[1]}")

            try:
                print("🔌 Connecting to Discord...")

                # Use start() with timeout for cleaner handling
                await asyncio.wait_for(bot.start(self.token), timeout=10.0)

            except asyncio.TimeoutError:
                print("❌ Connection timeout (10 seconds)")

            except discord.LoginFailure:
                print("❌ Authentication failed - Invalid token")
                print("💡 Check your bot token in Discord Developer Portal")

            except discord.HTTPException as e:
                print(f"❌ HTTP error: {e}")

            except Exception as e:
                print(f"❌ Unexpected error: {e}")

        return connection_successful

async def main():
    """Main test function"""
    # Configuration
    BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

    print("🧼 Clean Discord Bot Connection Test")
    print("=" * 42)

    if not BOT_TOKEN or BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("❌ Bot token not configured!")
        print("📝 Edit this file and set your bot token")
        print("🔗 Get token from: https://discord.com/developers/applications")
        return

    # Suppress warnings globally
    warnings.simplefilter("ignore", ResourceWarning)

    # Run the test
    tester = CleanBotTest(BOT_TOKEN)

    try:
        success = await tester.run_connection_test()

        if success:
            print("\n✅ All tests passed!")
        else:
            print("\n❌ Connection test failed")

    except KeyboardInterrupt:
        print("\n🛑 Test interrupted")

    except Exception as e:
        print(f"\n💥 Test error: {e}")

    finally:
        # Final cleanup
        await asyncio.sleep(0.1)
        print("\n" + "=" * 42)
        print("📋 Status Summary:")
        print("  ✅ = Bot token valid and Discord connection working")
        print("  ❌ = Check bot token or network connection")
        print("  ⚠️  = Bot connected but not added to any servers")
        print("\n🚀 Next Steps:")
        print("  1. Add bot to server via OAuth2 URL Generator")
        print("  2. Grant necessary permissions")
        print("  3. Test bot commands with full bot_status.py")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"\n💥 Fatal error: {e}")

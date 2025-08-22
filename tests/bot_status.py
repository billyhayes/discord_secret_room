import discord
from discord.ext import commands
import asyncio
import time

class BotStatusChecker:
    def __init__(self, token):
        self.token = token
        self.bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())
        self.setup_events()
        self.setup_commands()

    def setup_events(self):
        @self.bot.event
        async def on_ready():
            print(f'✅ {self.bot.user} has connected to Discord!')
            print(f'📊 Bot is in {len(self.bot.guilds)} servers')
            print(f'🆔 Bot ID: {self.bot.user.id}')
            print(f'⏰ Connected at: {time.strftime("%Y-%m-%d %H:%M:%S")}')

            # List all servers the bot is in
            if self.bot.guilds:
                print("\n🏠 Servers:")
                for guild in self.bot.guilds:
                    print(f"  - {guild.name} (ID: {guild.id}) - {guild.member_count} members")
            else:
                print("⚠️  Bot is not in any servers yet")

    def setup_commands(self):
        @self.bot.command(name='ping')
        async def ping_command(ctx):
            """Check bot latency and responsiveness"""
            start_time = time.time()
            message = await ctx.send("🏓 Pinging...")
            end_time = time.time()

            api_latency = round(self.bot.latency * 1000)
            response_time = round((end_time - start_time) * 1000)

            await message.edit(content=f"🏓 Pong!\n"
                                     f"📡 API Latency: {api_latency}ms\n"
                                     f"⚡ Response Time: {response_time}ms")

        @self.bot.command(name='status')
        async def status_command(ctx):
            """Comprehensive bot status check"""
            embed = discord.Embed(
                title="🤖 Bot Status Report",
                color=discord.Color.green(),
                timestamp=discord.utils.utcnow()
            )

            embed.add_field(
                name="📊 Connection Status",
                value=f"✅ Online\n🔗 Latency: {round(self.bot.latency * 1000)}ms",
                inline=True
            )

            embed.add_field(
                name="🏠 Server Info",
                value=f"🎯 Current Server: {ctx.guild.name}\n"
                      f"📈 Total Servers: {len(self.bot.guilds)}",
                inline=True
            )

            embed.add_field(
                name="👥 Members",
                value=f"👤 This Server: {ctx.guild.member_count}\n"
                      f"🌍 Total Reach: {sum(guild.member_count for guild in self.bot.guilds)}",
                inline=True
            )

            embed.set_footer(text=f"Bot ID: {self.bot.user.id}")
            await ctx.send(embed=embed)

        @self.bot.command(name='health')
        async def health_command(ctx):
            """Detailed health check"""
            health_status = "🟢 Healthy"
            issues = []

            # Check latency
            if self.bot.latency > 0.5:
                health_status = "🟡 Warning"
                issues.append(f"High latency: {round(self.bot.latency * 1000)}ms")

            # Check if bot can send messages
            try:
                test_message = await ctx.send("Testing message capabilities...")
                await test_message.delete()
            except Exception as e:
                health_status = "🔴 Critical"
                issues.append(f"Cannot send messages: {str(e)}")

            # Check permissions
            if not ctx.channel.permissions_for(ctx.guild.me).send_messages:
                health_status = "🟡 Warning"
                issues.append("Limited send message permissions")

            embed = discord.Embed(
                title="🏥 Bot Health Check",
                color=discord.Color.green() if health_status == "🟢 Healthy" else
                      discord.Color.yellow() if health_status == "🟡 Warning" else
                      discord.Color.red()
            )

            embed.add_field(name="Status", value=health_status, inline=False)

            if issues:
                embed.add_field(name="Issues Found", value="\n".join(issues), inline=False)
            else:
                embed.add_field(name="Issues Found", value="None - All systems operational! ✨", inline=False)

            await ctx.send(embed=embed)

        @self.bot.command(name='guilds')
        async def guilds_command(ctx):
            """List all servers the bot is in"""
            if not self.bot.guilds:
                await ctx.send("❌ Bot is not in any servers.")
                return

            embed = discord.Embed(
                title=f"🏠 Servers ({len(self.bot.guilds)})",
                color=discord.Color.blue()
            )

            for guild in self.bot.guilds:
                embed.add_field(
                    name=guild.name,
                    value=f"ID: {guild.id}\nMembers: {guild.member_count}",
                    inline=True
                )

            await ctx.send(embed=embed)

    async def run_tests(self):
        """Run automated connectivity tests"""
        print("🧪 Starting bot status tests...")

        try:
            # Test 1: Connection
            print("Test 1: Checking connection...")
            await self.bot.wait_until_ready()
            print("✅ Connection test passed")

            # Test 2: Latency check
            print("Test 2: Checking latency...")
            latency = self.bot.latency
            if latency < 0.1:
                print(f"✅ Latency test passed: {round(latency * 1000)}ms (Excellent)")
            elif latency < 0.3:
                print(f"⚠️ Latency test warning: {round(latency * 1000)}ms (Good)")
            else:
                print(f"❌ Latency test failed: {round(latency * 1000)}ms (Poor)")

            # Test 3: Guild access
            print("Test 3: Checking server access...")
            if self.bot.guilds:
                print(f"✅ Server access test passed: Connected to {len(self.bot.guilds)} servers")
            else:
                print("⚠️ Server access test warning: Not connected to any servers")

            print("🎉 All tests completed!")

            # Auto-close after tests complete
            await asyncio.sleep(2)
            await self.bot.close()

        except Exception as e:
            print(f"❌ Test failed with error: {e}")
        finally:
            if not self.bot.is_closed():
                await self.bot.close()

    def run(self):
        """Start the bot"""
        print("🚀 Starting Discord bot...")
        try:
            self.bot.run(self.token)
        except KeyboardInterrupt:
            print("🛑 Bot stopped by user")
        except Exception as e:
            print(f"❌ Bot error: {e}")
        finally:
            asyncio.run(self._cleanup())

    async def _cleanup(self):
        """Clean up connections"""
        if not self.bot.is_closed():
            await self.bot.close()
            print("🧹 Cleaned up bot connections")

# Example usage and test functions
async def quick_connection_test(token):
    """Quick test to verify bot can connect"""
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"✅ Quick test passed: {client.user} connected successfully!")
        print(f"📊 Connected to {len(client.guilds)} servers")
        await client.close()

    try:
        await client.start(token)
    except discord.LoginFailure:
        print("❌ Quick test failed: Invalid token")
    except Exception as e:
        print(f"❌ Quick test failed: {e}")
    finally:
        if not client.is_closed():
            await client.close()

if __name__ == "__main__":
    # Configuration
    BOT_TOKEN = ""  # Replace with your actual bot token

    # Uncomment one of the following options:

    # Option 1: Run the full bot with commands
    bot_checker = BotStatusChecker(BOT_TOKEN)
    bot_checker.run()

    # Option 2: Run quick connection test
    # try:
    #     asyncio.run(quick_connection_test(BOT_TOKEN))
    # except KeyboardInterrupt:
    #     print("🛑 Test stopped by user")

    # Option 3: Run automated tests only
    # bot_checker = BotStatusChecker(BOT_TOKEN)
    # try:
    #     asyncio.run(bot_checker.run_tests())
    # except KeyboardInterrupt:
    #     print("🛑 Tests stopped by user")

    # Instructions are shown below when the bot is not running
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("🔧 Bot status checker ready!")
        print("📝 Instructions:")
        print("1. Replace 'YOUR_BOT_TOKEN_HERE' with your actual bot token")
        print("2. Uncomment one of the options above")
        print("3. Run the script")
        print("\n💡 Available commands when bot is running:")
        print("  !ping - Check latency")
        print("  !status - Comprehensive status report")
        print("  !health - Detailed health check")
        print("  !guilds - List all servers")

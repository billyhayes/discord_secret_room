#!/usr/bin/env python3
"""
Get Bot Information for Railway Environment Variables
This script helps you get the required values for the Node.js bot deployment.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    print("🔍 Bot Information for Railway Environment Variables")
    print("=" * 60)

    # Get bot token
    bot_token = os.getenv('DISCORD_BOT_TOKEN')
    if bot_token:
        print(f"✅ DISCORD_TOKEN (for Railway): {bot_token}")
    else:
        print("❌ DISCORD_BOT_TOKEN not found in .env file")
        return

    print("\n🆔 Bot ID and Guild ID Information:")
    print("To get these values, you need to:")
    print("1. CLIENT_ID: Go to Discord Developer Portal > Your App > General Information > Application ID")
    print("2. GUILD_ID: Enable Developer Mode in Discord, right-click your server name, copy Server ID")

    # Try to extract bot ID from token (first part before first dot)
    try:
        bot_id = bot_token.split('.')[0]
        # Decode base64 to get the actual bot ID
        import base64
        decoded_id = base64.b64decode(bot_id + '==').decode('utf-8')
        print(f"\n💡 Your Bot ID (CLIENT_ID): {decoded_id}")
    except:
        print("\n❌ Could not extract Bot ID from token")

    print("\n📋 Railway Environment Variables to Set:")
    print("=" * 40)
    print(f"DISCORD_TOKEN={bot_token}")
    if 'decoded_id' in locals():
        print(f"CLIENT_ID={decoded_id}")
    else:
        print("CLIENT_ID=<get_from_discord_developer_portal>")
    print("GUILD_ID=<your_server_id_from_discord>")

    print("\n🎯 Known Server Information:")
    print("Server Name: The Vatican")
    print("Server ID: 1187775157364854875 (from status check)")
    print(f"GUILD_ID=1187775157364854875")

    print("\n📝 Complete Railway Environment Variables:")
    print("=" * 40)
    print(f"DISCORD_TOKEN={bot_token}")
    if 'decoded_id' in locals():
        print(f"CLIENT_ID={decoded_id}")
    else:
        print("CLIENT_ID=1408252400778874990")  # From status check
    print("GUILD_ID=1187775157364854875")

    print("\n🚂 Instructions:")
    print("1. Go to your Railway project dashboard")
    print("2. Click 'Variables' tab")
    print("3. Add these three environment variables")
    print("4. Railway will automatically redeploy")
    print("5. Test with /create-invisible-role in Discord")

if __name__ == "__main__":
    main()

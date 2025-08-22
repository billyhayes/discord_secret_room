# Discord Bot Testing Tools

This directory contains testing utilities for the Discord bot.

## Status Checker

The `status_check.py` script is a minimal Discord bot status checker that verifies if your bot is online and working properly.

### Setup

1. **Install dependencies:**
   ```bash
   pip install -r ../requirements.txt
   ```

2. **Configure your bot token:**
   
   **Option A: Using .env file (Recommended)**
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env and add your actual bot token
   # DISCORD_BOT_TOKEN=your_actual_bot_token_here
   ```

   **Option B: Environment variable**
   ```bash
   export DISCORD_BOT_TOKEN=your_bot_token_here
   ```

   **Option C: Command line argument**
   ```bash
   python3 status_check.py your_bot_token_here
   ```

### Usage

Run the status checker:

```bash
python3 status_check.py
```

### What it checks

- ✅ Bot authentication and connection
- 🤖 Bot information (name, ID, discriminator)
- 📡 Connection latency
- 🏠 Server membership and member counts
- ⚠️  Common connection issues

### Sample Output

```
🤖 Discord Bot Status Checker
==================================================
🔍 Checking Discord bot status...
🔑 Using token from .env file

==================================================
📊 BOT STATUS REPORT
==================================================
✅ Status: ONLINE
🤖 Bot: MyBot#1234
🆔 ID: 123456789012345678
📡 Latency: 45.2ms
🏠 Servers: 3

📋 Server List:
  • My Test Server (150 members)
  • Development Server (5 members)
  • Bot Testing (2 members)

⏰ Check time: 2024-01-15 14:30:25
==================================================
```

### Troubleshooting

If the bot shows as offline:

1. **Verify bot token is correct**
   - Check Discord Developer Portal
   - Try regenerating the token if needed

2. **Check bot permissions**
   - Ensure bot has necessary intents enabled
   - Verify OAuth2 scopes are correct

3. **Network connectivity**
   - Check internet connection
   - Verify no firewall blocking Discord

### Security Notes

- Never commit your `.env` file to version control
- The `.env` file is already included in `.gitignore`
- Keep your bot token private and secure
- Regenerate your token if it gets exposed

### Getting Your Bot Token

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Select your application
3. Go to the "Bot" section
4. Copy the token under "Token"
5. Add it to your `.env` file

### Files

- `status_check.py` - Main status checker script
- `.env.example` - Template for environment variables
- `README.md` - This documentation
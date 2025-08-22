# Discord Secret Room Bot 🤖

A comprehensive Discord bot built with Python and discord.py, designed for deployment on Railway. This bot provides utility commands, server management features, and interactive functionality for Discord servers.

## 🎯 Features

- **Always Online** - Deployed on Railway with automatic restarts
- **Interactive Commands** - Ping, status, server info, user info, and more
- **Fun Commands** - Dice rolling, coin flipping, echo messages
- **Admin Tools** - Message cleaning and moderation features
- **Health Monitoring** - Built-in status checking and diagnostics
- **Permission Management** - Comprehensive permission system

## 🚀 Quick Start

### Local Development

1. **Clone and setup environment:**
   ```bash
   cd discord_secret_room
   python3 -m venv discord_bot_env
   source discord_bot_env/bin/activate  # On Windows: discord_bot_env\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Set your bot token:**
   ```bash
   export DISCORD_BOT_TOKEN="your_bot_token_here"
   ```

3. **Run the bot:**
   ```bash
   python3 start.py
   ```

### Railway Deployment

1. **Connect to Railway:**
   - Go to [Railway Dashboard](https://railway.app/dashboard)
   - Click "New Project" → "Deploy from GitHub repo"
   - Select this repository

2. **Set environment variables in Railway:**
   ```
   DISCORD_BOT_TOKEN = your_discord_bot_token
   COMMAND_PREFIX = !
   RAILWAY_ENVIRONMENT = production
   PYTHONUNBUFFERED = 1
   ```

3. **Deploy:**
   Railway automatically detects and deploys using `start.py`

## 📋 Available Commands

| Command | Description | Example |
|---------|-------------|---------|
| `!ping` | Check bot latency and connection | `!ping` |
| `!hello` | Friendly greeting | `!hello` |
| `!status` | Comprehensive bot status | `!status` |
| `!server` | Display server information | `!server` |
| `!user` | Show user information | `!user @someone` |
| `!roll` | Roll a dice (default 6 sides) | `!roll 20` |
| `!flip` | Flip a coin | `!flip` |
| `!echo` | Echo back a message | `!echo Hello World` |
| `!railway` | Railway deployment info | `!railway` |
| `!clean` | Clean messages (admin only) | `!clean 5` |
| `!help` | Show all commands | `!help` |

## 🗂️ Project Structure

```
discord_secret_room/
├── start.py                 # Main bot entry point (Railway)
├── interactive_bot.py       # Local development bot
├── Procfile                 # Railway process definition
├── requirements.txt         # Python dependencies
├── railway.json            # Railway configuration
├── package.json            # Node.js metadata (legacy)
├── index.js                # Node.js version (legacy)
├── railway.toml            # Railway settings
├── 
├── tests/                  # Bot testing utilities
│   ├── bot_status.py       # Comprehensive bot status checker
│   ├── simple_bot_test.py  # Simple connection test
│   ├── clean_bot_test.py   # Clean connection test
│   └── status_check.py     # Minimal status checker
│
├── utils/                  # Utility scripts
│   ├── decode_permissions.py    # Permission decoder
│   └── generate_invite.py       # OAuth2 URL generator
│
├── scripts/                # Helper scripts
│   └── activate_env.sh     # Environment activation
│
├── docs/                   # Documentation
│   ├── RAILWAY_DEPLOYMENT.md   # Complete Railway guide
│   └── bot_permissions_guide.md # Permission reference
│
├── deployment/             # Deployment configurations
│   ├── Dockerfile          # Docker container setup
│   └── docker-compose.yml  # Multi-service deployment
│
└── README.md              # This file
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `DISCORD_BOT_TOKEN` | Your Discord bot token | None | ✅ Yes |
| `COMMAND_PREFIX` | Bot command prefix | `!` | No |
| `RAILWAY_ENVIRONMENT` | Deployment environment | `production` | No |
| `PYTHONUNBUFFERED` | Python output buffering | `1` | No |

### Bot Permissions

The bot requires these Discord permissions:
- View Channels
- Send Messages
- Read Message History
- Embed Links
- Use External Emojis
- Add Reactions
- Use Slash Commands

**Generate invite URL:**
```bash
python3 utils/generate_invite.py YOUR_CLIENT_ID essential
```

## 🔧 Development

### Testing

**Quick connection test:**
```bash
python3 tests/status_check.py
```

**Comprehensive testing:**
```bash
python3 tests/bot_status.py
```

**Permission debugging:**
```bash
python3 utils/decode_permissions.py 2147830848
```

### Local Development

1. **Activate environment:**
   ```bash
   source scripts/activate_env.sh
   ```

2. **Run interactive bot:**
   ```bash
   python3 interactive_bot.py
   ```

3. **Test commands in Discord:**
   - `!ping` - Verify connection
   - `!status` - Check bot health

## 🚂 Railway Deployment

This bot is optimized for Railway deployment:

- **Automatic startup** via `start.py`
- **Environment variable configuration**
- **Built-in logging and monitoring**
- **Auto-restart on crashes**
- **Scalable architecture**

### Deployment Steps

1. Push code to GitHub
2. Connect Railway to repository  
3. Set environment variables
4. Deploy automatically

See [docs/RAILWAY_DEPLOYMENT.md](docs/RAILWAY_DEPLOYMENT.md) for complete guide.

## 📊 Monitoring

### Health Checks

The bot includes several health monitoring features:

- **Connection status** - Real-time Discord connection
- **Latency monitoring** - Response time tracking
- **Server count** - Guild membership tracking  
- **Error logging** - Comprehensive error handling

### Commands for Monitoring

- `!ping` - Basic connectivity test
- `!status` - Detailed status report
- `!railway` - Railway-specific metrics

## 🛡️ Security

- **Token security** - Never commit tokens to git
- **Permission system** - Role-based command access
- **Input validation** - Sanitized user inputs
- **Error handling** - Graceful failure management

## 📖 Documentation

- [Railway Deployment Guide](docs/RAILWAY_DEPLOYMENT.md) - Complete deployment instructions
- [Bot Permissions Guide](docs/bot_permissions_guide.md) - Permission reference
- [Discord.py Documentation](https://discordpy.readthedocs.io/) - Library reference

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

### Bot Information
- **Bot Name:** secret_room#7956
- **Bot ID:** 1408252400778874990
- **Current Status:** ✅ Online (Railway)
- **Command Prefix:** `!`

### Getting Help
- Use `!help` command in Discord
- Check [Railway Dashboard](https://railway.app/dashboard) for deployment status
- Review logs for debugging information

### Common Issues

**Bot not responding:**
1. Check Railway deployment status
2. Verify `DISCORD_BOT_TOKEN` environment variable
3. Test with `!ping` command
4. Review deployment logs

**Permission errors:**
1. Check bot permissions in server settings
2. Use `utils/generate_invite.py` to generate new invite URL
3. Re-invite bot with updated permissions

## 🎉 Features Roadmap

- [ ] Database integration (PostgreSQL)
- [ ] Slash commands implementation  
- [ ] Advanced moderation tools
- [ ] Music playback features
- [ ] Custom server configurations
- [ ] Analytics dashboard
- [ ] Multi-language support

---

**Ready to deploy?** Follow the [Railway Deployment Guide](docs/RAILWAY_DEPLOYMENT.md) to get your bot online! 🚀

**Need help?** Use `!help` in Discord or check the documentation in the `docs/` folder.# Updated Fri Aug 22 01:27:10 CDT 2025

# Discord Invisible Roles & Rooms Bot 👻

A Discord bot that creates invisible rooms (channels) and invisible roles for your server. Perfect for creating secret channels, staff areas, or hidden community spaces.

## Features

- 🎭 **Invisible Roles**: Create roles that don't appear in the member list and can't be mentioned
- 🔒 **Invisible Channels**: Create channels that are completely hidden from unauthorized users
- 👑 **Admin Only**: All commands require Administrator permissions for security
- 📝 **Slash Commands**: Modern Discord slash command interface
- 📊 **Management Tools**: List and manage all invisible elements

## Quick Start

### Prerequisites

- Node.js 16.11.0 or higher
- A Discord bot token
- Administrator permissions on your Discord server

### Installation

1. **Clone or download this project**

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and fill in your bot credentials:
   ```env
   DISCORD_TOKEN=your_bot_token_here
   CLIENT_ID=your_bot_client_id_here
   GUILD_ID=your_server_guild_id_here
   DEBUG=false
   ```

4. **Run the bot**
   ```bash
   npm start
   ```

## Discord Bot Setup

### Creating a Bot

1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to the "Bot" section
4. Click "Add Bot"
5. Copy the token and add it to your `.env` file as `DISCORD_TOKEN`
6. Copy the Application ID and add it to your `.env` file as `CLIENT_ID`

### Getting Guild ID

1. Enable Developer Mode in Discord (User Settings → Advanced → Developer Mode)
2. Right-click your server name and select "Copy Server ID"
3. Add this to your `.env` file as `GUILD_ID`

### Bot Permissions

When inviting your bot to your server, make sure it has these permissions:
- `Manage Roles`
- `Manage Channels`
- `View Channels`
- `Send Messages`
- `Use Slash Commands`

**Invite URL Template:**
```
https://discord.com/api/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=268435472&scope=bot%20applications.commands
```

## Commands

All commands are slash commands and require Administrator permissions.

### `/create-invisible-role`
Creates an invisible role that won't appear in the member list.

**Parameters:**
- `name` (required): Name of the role
- `color` (optional): Hex color code (e.g., #ff0000)

**Example:**
```
/create-invisible-role name:Secret Staff color:#ff0000
```

### `/create-invisible-room`
Creates an invisible channel that only specific roles can see.

**Parameters:**
- `name` (required): Name of the channel
- `role` (required): Role that can access the channel
- `type` (optional): Channel type (text or voice, defaults to text)

**Example:**
```
/create-invisible-room name:staff-secret role:@Secret Staff type:text
```

### `/assign-invisible-role`
Assigns an invisible role to a user.

**Parameters:**
- `user` (required): User to assign the role to
- `role` (required): Invisible role to assign

**Example:**
```
/assign-invisible-role user:@JohnDoe role:@Secret Staff
```

### `/list-invisible`
Lists all invisible roles and channels in the server.

**Example:**
```
/list-invisible
```

## How It Works

### Invisible Roles
- `hoist: false` - Role doesn't appear separately in member list
- `mentionable: false` - Role can't be mentioned by regular users
- No special permissions by default
- Members with these roles appear as regular members in the list

### Invisible Channels
- Permission overwrites deny `@everyone` from viewing the channel
- Only specified roles can see and interact with the channel
- Completely hidden from unauthorized users
- Works for both text and voice channels

## Security Features

- ✅ Administrator permissions required for all commands
- ✅ Proper permission validation
- ✅ Error handling and user feedback
- ✅ Audit logging with command attribution
- ✅ Ephemeral responses (only command user sees results)

## Troubleshooting

### Bot Not Responding
- Check if the bot is online in your server
- Verify the bot has proper permissions
- Check console for error messages
- Ensure slash commands are registered (happens automatically on startup)

### Commands Not Appearing
- Wait a few minutes after starting the bot
- Make sure you have Administrator permissions
- Try refreshing Discord or relogging

### Permission Errors
- Ensure the bot's role is higher than roles it's trying to manage
- Verify the bot has `Manage Roles` and `Manage Channels` permissions
- Check that the bot can see the channels it's working with

## Development

### Running in Development Mode
```bash
npm run dev
```

### Environment Variables
- `DEBUG=true` - Enable additional logging
- All other variables are required for the bot to function

### File Structure
```
discord/thunderdome/
├── index.js          # Main bot file
├── package.json      # Dependencies and scripts
├── .env.example      # Environment template
├── .env             # Your environment variables (not tracked)
└── README.md        # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - feel free to use this bot in your own servers!

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review console logs for error messages
3. Verify all permissions and setup steps
4. Check Discord's API status

## 🚀 Railway Deployment

This bot is optimized for Railway deployment - the best free hosting option for Discord bots!

### ⚡ Quick Deploy to Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/discord-bot)

### 📋 Step-by-Step Railway Deployment

#### 1. 🔧 **Prepare Your Repository**
```bash
# Push your code to GitHub if you haven't already
git init
git add .
git commit -m "Initial Discord Invisible Bot"
git branch -M main
git remote add origin https://github.com/yourusername/discord-invisible-bot.git
git push -u origin main
```

#### 2. 🚂 **Create Railway Account**
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub (recommended for easy repo access)
3. Verify your account

#### 3. 📦 **Deploy from GitHub**
1. Click **"New Project"** in Railway dashboard
2. Select **"Deploy from GitHub repo"**
3. Choose your bot repository
4. Railway will automatically detect it's a Node.js app

#### 4. 🔑 **Configure Environment Variables**
In your Railway project dashboard:
1. Go to **Variables** tab
2. Add these environment variables:
   ```
   DISCORD_TOKEN=your_bot_token_here
   CLIENT_ID=your_bot_client_id_here
   GUILD_ID=your_server_guild_id_here
   DEBUG=false
   ```

#### 5. 🚀 **Deploy**
Railway will automatically:
- Install dependencies (`npm install`)
- Start your bot (`npm start`)
- Generate a public URL
- Monitor and restart if needed

### 📊 Railway Benefits
- ✅ **$5/month credit** (enough for most Discord bots)
- ✅ **24/7 uptime** (no sleeping)
- ✅ **Auto-deploy** on git push
- ✅ **Zero configuration** needed
- ✅ **Built-in monitoring** and logs
- ✅ **Custom domains** available

### 🔍 **Monitoring Your Bot**
In Railway dashboard:
- **Deployments**: See build logs and status
- **Metrics**: Monitor CPU, memory, and bandwidth
- **Logs**: View real-time bot output
- **Variables**: Update environment variables

### 🔄 **Auto-Deploy Setup**
Railway automatically redeploys when you push to your GitHub main branch:
```bash
# Make changes to your bot
git add .
git commit -m "Update bot features"
git push origin main
# Railway automatically deploys the changes!
```

### 🛠️ **Local Development**
Test locally before deploying:
```bash
# Install dependencies
npm install

# Copy environment template
cp .env.example .env
# Edit .env with your bot credentials

# Run locally
npm start
```

### 💰 **Cost Management**
- **Free tier**: $5/month credit
- **Usage tracking**: Monitor in Railway dashboard
- **Upgrade**: Add payment method for additional credits
- **Optimization**: Bot typically uses $1-3/month

### ❗ **Troubleshooting Railway**
- **Bot not starting**: Check logs in Railway dashboard
- **Commands not working**: Verify environment variables
- **Build failing**: Check package.json and dependencies
- **Out of credits**: Add payment method or optimize usage

### 🔐 **Security Best Practices**
- ✅ **Never commit** `.env` files to GitHub
- ✅ **Use Railway Variables** for sensitive data
- ✅ **Regenerate tokens** if accidentally exposed
- ✅ **Monitor bot usage** in Discord Developer Portal
- ✅ **Keep dependencies updated** regularly

---

## 📱 **Alternative Deployment Options**

### 🏠 Local Development
```bash
npm start  # For testing only
```

### 🎨 Other Cloud Platforms
- **Render**: Free tier with sleep
- **Glitch**: Free with CPU limits
- **DigitalOcean**: $5/month VPS
- **AWS EC2**: Enterprise option

**👑 Railway is recommended** for the best balance of features, reliability, and cost.

---

**⚠️ Security Note**: Keep your bot token secure and never share it publicly. Anyone with your bot token can control your bot.

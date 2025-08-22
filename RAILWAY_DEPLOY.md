# 🚂 Railway Deployment Guide

Complete step-by-step guide to deploy your Discord Invisible Bot on Railway.

## 🎯 Prerequisites

- Discord bot created in [Discord Developer Portal](https://discord.com/developers/applications)
- GitHub account
- Code pushed to a GitHub repository

## 📋 Step 1: Get Discord Bot Credentials

### Create Discord Application
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click **"New Application"**
3. Name your application (e.g., "Invisible Bot")
4. Go to **"Bot"** section
5. Click **"Add Bot"**
6. Copy the **Token** - this is your `DISCORD_TOKEN`
7. Go to **"General Information"**
8. Copy the **Application ID** - this is your `CLIENT_ID`

### Get Server Guild ID
1. Enable Developer Mode in Discord:
   - User Settings → Advanced → Developer Mode ✅
2. Right-click your server name
3. Select **"Copy Server ID"** - this is your `GUILD_ID`

### Bot Permissions
Your bot needs these permissions:
- ✅ Manage Roles
- ✅ Manage Channels
- ✅ View Channels
- ✅ Send Messages
- ✅ Use Slash Commands

**Invite URL Template:**
```
https://discord.com/api/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=268435472&scope=bot%20applications.commands
```

Replace `YOUR_CLIENT_ID` with your actual Client ID.

## 🚂 Step 2: Deploy on Railway

### Create Railway Account
1. Go to [railway.app](https://railway.app)
2. Click **"Sign up with GitHub"** (recommended)
3. Authorize Railway to access your repositories

### Deploy from GitHub
1. Click **"New Project"** in Railway dashboard
2. Select **"Deploy from GitHub repo"**
3. Choose your Discord bot repository
4. Railway automatically detects it's a Node.js project

### Configure Environment Variables
1. In your Railway project, go to **"Variables"** tab
2. Add these variables one by one:

```
DISCORD_TOKEN=your_bot_token_here
CLIENT_ID=your_bot_client_id_here
GUILD_ID=your_server_guild_id_here
DEBUG=false
```

⚠️ **Never share these values publicly!**

## 🔧 Step 3: Monitor Deployment

### Check Build Logs
1. Go to **"Deployments"** tab
2. Click on the latest deployment
3. Watch the build process:
   ```
   Installing dependencies...
   npm install
   
   Starting application...
   npm start
   
   Health check server running on port 3000
   Logged in as YourBot#1234!
   Successfully reloaded application (/) commands.
   ```

### Health Check
Railway will automatically check if your bot is healthy at `/health` endpoint.

### View Logs
- Real-time logs available in **"Logs"** section
- Monitor bot activity and errors
- Check Discord connection status

## ✅ Step 4: Verify Bot is Working

### Test Commands
In your Discord server, try:
```
/create-invisible-role name:"Secret Staff" color:#ff0000
/create-invisible-room name:"staff-hideout" role:@Secret Staff
/list-invisible
```

### Bot Status
- Bot should show as **Online** in your server
- Commands should appear when typing `/`
- Health endpoint should return: `Discord Invisible Bot is running! 👻`

## 🔄 Step 5: Auto-Deploy Setup

Railway automatically redeploys when you push to GitHub:

```bash
# Make changes to your bot
git add .
git commit -m "Add new features"
git push origin main
# Railway automatically builds and deploys!
```

## 💰 Cost Management

### Free Tier
- **$5/month credit** included
- Typically uses **$1-3/month** for Discord bots
- Monitor usage in Railway dashboard

### Usage Optimization
- Bot uses minimal resources when idle
- No additional charges for slash commands
- Health checks use negligible bandwidth

### Upgrade Options
- Add payment method for additional credits
- Scale resources if needed (rarely required for Discord bots)

## 🛠️ Troubleshooting

### Bot Not Starting
**Check:** Environment variables in Railway
```
Variables tab → Verify all 4 variables are set correctly
```

**Check:** Build logs for errors
```
Deployments tab → Latest deployment → Build logs
```

### Commands Not Appearing
**Wait:** Slash commands take 1-3 minutes to register
**Check:** Bot has proper permissions in your server
**Verify:** GUILD_ID matches your server

### Permission Errors
**Ensure:** Bot role is higher than roles it manages
**Check:** Bot has "Manage Roles" and "Manage Channels" permissions
**Verify:** Bot was invited with correct permission URL

### Build Failures
**Check:** `package.json` syntax is valid
**Verify:** All dependencies are properly listed
**Review:** Build logs for specific error messages

## 🔐 Security Best Practices

### Environment Variables
- ✅ **Never commit** `.env` files to GitHub
- ✅ **Use Railway Variables** for all sensitive data
- ✅ **Regenerate tokens** if accidentally exposed
- ✅ **Keep `.gitignore` updated** to exclude secrets

### Bot Token Security
- 🚫 Never share bot token publicly
- 🔄 Regenerate token if compromised
- 🔒 Only use Railway Variables for storage
- 📝 Monitor bot usage in Discord Developer Portal

## 📊 Monitoring & Maintenance

### Railway Dashboard
- **Metrics**: Monitor CPU, memory, network usage
- **Logs**: Real-time application logs
- **Deployments**: Track build history
- **Variables**: Update configuration safely

### Bot Health
- Health endpoint: `https://your-railway-app.railway.app/health`
- Returns bot connection status and uptime
- Automatic restart on failure

### Updates & Maintenance
- Push updates to GitHub for auto-deployment
- Monitor Discord API changes
- Keep dependencies updated regularly
- Review logs for any issues

## 🎉 Success!

Your Discord Invisible Bot is now running 24/7 on Railway! 

### What's Next?
- Invite friends to test invisible features
- Create more invisible channels for different purposes  
- Monitor usage and costs in Railway dashboard
- Customize bot features as needed

### Need Help?
- Railway Discord: [discord.gg/railway](https://discord.gg/railway)
- Railway Docs: [docs.railway.app](https://docs.railway.app)
- Bot Issues: Check GitHub repository issues

---

**🎯 Pro Tip**: Bookmark your Railway dashboard and Discord Developer Portal for easy access to logs and bot management!
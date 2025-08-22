# Railway Deployment Guide 🚂

Complete guide to deploy your Discord bot `secret_room#7956` to Railway.

## 📋 Prerequisites

- [x] Railway account (sign up at https://railway.app)
- [x] GitHub account 
- [x] Discord bot token
- [x] Your bot code ready

## 🚀 Quick Deployment Steps

### Step 1: Prepare Your Repository

1. **Ensure these files exist in your project:**
   ```
   discord/
   ├── start.py              # ✅ Main bot file (Railway entry point)
   ├── requirements.txt      # ✅ Python dependencies
   ├── Procfile             # ✅ Railway process definition
   ├── railway.json         # ✅ Railway configuration
   └── README.md            # Optional but recommended
   ```

2. **Commit and push to GitHub:**
   ```bash
   git add .
   git commit -m "Prepare for Railway deployment"
   git push origin main
   ```

### Step 2: Deploy to Railway

1. **Go to Railway Dashboard:**
   - Visit https://railway.app/dashboard
   - Click "New Project"

2. **Connect GitHub Repository:**
   - Click "Deploy from GitHub repo"
   - Select your repository
   - Choose the `discord` folder if prompted

3. **Set Environment Variables:**
   - Go to your project → Variables tab
   - Add these variables:
     ```
     DISCORD_BOT_TOKEN = ***REMOVED***
     COMMAND_PREFIX = !
     RAILWAY_ENVIRONMENT = production
     PYTHONUNBUFFERED = 1
     ```

4. **Deploy:**
   - Railway will automatically detect and deploy your bot
   - Watch the deployment logs in real-time

### Step 3: Verify Deployment

1. **Check Deployment Logs:**
   - Look for: `🤖 DISCORD BOT DEPLOYED ON RAILWAY!`
   - Verify bot connection to Discord

2. **Test Bot Commands:**
   - Go to your Discord server ("The Vatican")
   - Try `!ping`, `!status`, `!railway`

## ⚙️ Configuration Options

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `DISCORD_BOT_TOKEN` | Your Discord bot token | ✅ Yes | None |
| `COMMAND_PREFIX` | Bot command prefix | No | `!` |
| `RAILWAY_ENVIRONMENT` | Deployment environment | No | `production` |
| `PYTHONUNBUFFERED` | Python output buffering | No | `1` |
| `TZ` | Timezone | No | `UTC` |

### Railway Settings

**Recommended settings in Railway dashboard:**

- **Region:** `us-west1` (or closest to your users)
- **Memory:** `512MB` (sufficient for most bots)
- **Restart Policy:** `ON_FAILURE`
- **Healthcheck:** Enabled (automatic)

## 🔧 Advanced Configuration

### Custom Domains (Railway Pro)

1. Go to Settings → Networking
2. Add custom domain
3. Configure DNS records as shown

### Database Integration

If you need database storage:

1. **Add PostgreSQL:**
   ```bash
   # In Railway dashboard
   Add Service → PostgreSQL
   ```

2. **Update your bot code:**
   ```python
   import os
   import psycopg2
   
   DATABASE_URL = os.getenv('DATABASE_URL')
   # Use database in your bot commands
   ```

### Redis Cache

For caching/sessions:

1. **Add Redis:**
   ```bash
   # In Railway dashboard
   Add Service → Redis
   ```

2. **Connection example:**
   ```python
   import redis
   
   REDIS_URL = os.getenv('REDIS_URL')
   r = redis.from_url(REDIS_URL)
   ```

## 🐛 Troubleshooting

### Common Issues

**1. Bot Not Starting**
```
Error: DISCORD_BOT_TOKEN environment variable not found!
```
**Solution:** Set `DISCORD_BOT_TOKEN` in Railway variables

**2. Import Errors**
```
ModuleNotFoundError: No module named 'discord'
```
**Solution:** Ensure `requirements.txt` includes `discord.py==2.6.0`

**3. Permission Errors**
```
403 Forbidden (error code: 50013)
```
**Solution:** Check bot permissions in Discord server

**4. Connection Issues**
```
[Errno 11001] getaddrinfo failed
```
**Solution:** Network issue, usually resolves automatically

### Deployment Logs

**Healthy deployment looks like:**
```
=== Building ===
Installing dependencies...
✅ discord.py installed
✅ Requirements satisfied

=== Deploying ===
🚀 Starting Discord Bot on Railway...
🤖 DISCORD BOT DEPLOYED ON RAILWAY!
✅ Connected to Discord
📋 Server List:
  • The Vatican (25 members)
🎯 Bot is ready for commands!
```

**Check logs in Railway:**
- Dashboard → Your Project → Deployments → View Logs

### Bot Status Commands

Use these commands to debug:

- `!ping` - Check latency and connection
- `!status` - Comprehensive bot status
- `!railway` - Railway-specific information

## 📊 Monitoring & Maintenance

### Automatic Restarts

Railway automatically restarts your bot if it crashes:
- **Restart Policy:** `ON_FAILURE`
- **Max Retries:** 3
- **Restart Delay:** 5 seconds

### Logs and Monitoring

1. **View Real-time Logs:**
   - Railway Dashboard → Your Project → Logs

2. **Monitor Resource Usage:**
   - Dashboard → Metrics tab
   - Watch CPU, Memory, Network usage

3. **Set Up Alerts (Pro):**
   - Configure notifications for downtime
   - Email/Slack integration available

### Updates and Redeployment

**Automatic Updates:**
- Push to GitHub main branch
- Railway auto-deploys new changes

**Manual Redeploy:**
- Railway Dashboard → Redeploy button
- Useful for environment variable changes

## 💰 Pricing & Limits

### Railway Free Tier
- **Usage:** $5 credit monthly
- **Sleep Policy:** No sleeping for Discord bots
- **Bandwidth:** Generous limits
- **Perfect for:** Personal bots, testing

### Railway Pro Plan
- **Usage:** Pay-as-you-go after credit
- **Features:** Custom domains, priority support
- **Cost:** ~$5-10/month for typical Discord bot

### Cost Optimization

1. **Optimize Memory Usage:**
   - Monitor memory in Dashboard
   - Typical Discord bot uses 50-200MB

2. **Reduce CPU Usage:**
   - Efficient command handling
   - Avoid infinite loops

## 🎯 Production Checklist

Before going live:

- [ ] Bot token is secure (not in code)
- [ ] Environment variables configured
- [ ] Bot tested in development server
- [ ] Error handling implemented
- [ ] Logging configured
- [ ] Bot permissions set correctly
- [ ] Railway deployment successful
- [ ] Bot responds to commands
- [ ] Monitor logs for issues

## 🆘 Support & Resources

### Railway Support
- **Documentation:** https://docs.railway.app
- **Community:** Discord server (railway.app/discord)
- **Help Center:** help.railway.app

### Discord Bot Support
- **Discord.py Docs:** https://discordpy.readthedocs.io
- **Discord Developer Portal:** https://discord.com/developers

### Your Bot Status
- **Bot Name:** secret_room#7956
- **Bot ID:** 1408252400778874990
- **Current Server:** The Vatican (25 members)
- **Commands:** !ping, !status, !railway, !help

---

## 🎉 Success!

Your Discord bot is now deployed on Railway! 

**Test it:**
1. Go to your Discord server
2. Type `!ping` 
3. Bot should respond with latency info

**Monitor it:**
- Railway Dashboard for deployment status
- Discord server for bot online status
- Bot commands for health checks

Your bot will automatically start when Railway deploys and restart if it ever crashes. Enjoy your always-online Discord bot! 🚀
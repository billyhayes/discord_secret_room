# 🚀 Railway Deployment Checklist

Quick reference checklist to deploy your Discord Invisible Bot on Railway.

## ✅ Pre-Deployment Checklist

### Discord Bot Setup
- [ ] Created Discord application at [discord.com/developers/applications](https://discord.com/developers/applications)
- [ ] Generated bot token (DISCORD_TOKEN)
- [ ] Copied application ID (CLIENT_ID)
- [ ] Got server Guild ID (GUILD_ID)
- [ ] Invited bot to server with permissions:
  - [ ] Manage Roles
  - [ ] Manage Channels
  - [ ] View Channels
  - [ ] Send Messages
  - [ ] Use Slash Commands

### Code Repository
- [ ] Code pushed to GitHub repository
- [ ] `.env` file is NOT committed (in `.gitignore`)
- [ ] All dependencies listed in `package.json`
- [ ] `railway.toml` configuration file present

## 🚂 Railway Deployment Steps

### Account & Project Setup
- [ ] Created Railway account at [railway.app](https://railway.app)
- [ ] Connected GitHub account to Railway
- [ ] Created new project from GitHub repo
- [ ] Railway detected Node.js project automatically

### Environment Variables Configuration
Add these 4 variables in Railway Variables tab:
- [ ] `DISCORD_TOKEN` = your_bot_token_here
- [ ] `CLIENT_ID` = your_bot_client_id_here  
- [ ] `GUILD_ID` = your_server_guild_id_here
- [ ] `DEBUG` = false

### Deployment Verification
- [ ] Build completed successfully (check Deployments tab)
- [ ] Health check endpoint responding at `/health`
- [ ] Bot shows as Online in Discord server
- [ ] Slash commands registered and visible

## 🧪 Testing Checklist

### Command Testing
Test each command in your Discord server:
- [ ] `/create-invisible-role name:"Test Role" color:#ff0000`
- [ ] `/create-invisible-room name:"test-room" role:@TestRole`
- [ ] `/assign-invisible-role user:@YourUsername role:@TestRole`
- [ ] `/list-invisible`

### Functionality Verification
- [ ] Invisible role doesn't appear in member list
- [ ] Invisible channel only visible to assigned role
- [ ] Commands require Administrator permissions
- [ ] Error handling works (try invalid inputs)

## 📊 Post-Deployment Monitoring

### Railway Dashboard
- [ ] Bookmarked Railway project dashboard
- [ ] Checked initial resource usage
- [ ] Verified auto-deploy is working
- [ ] Set up monitoring alerts (if needed)

### Bot Health
- [ ] Health endpoint returns correct status
- [ ] Bot logs show no errors
- [ ] Discord connection stable
- [ ] Commands responding quickly

## 🔧 Troubleshooting Quick Fixes

### Bot Not Online
- [ ] Check DISCORD_TOKEN is correct
- [ ] Verify bot has proper server permissions
- [ ] Review Railway logs for connection errors

### Commands Not Working
- [ ] Wait 2-3 minutes for slash command registration
- [ ] Check GUILD_ID matches your server
- [ ] Verify CLIENT_ID is correct
- [ ] Ensure user has Administrator permissions

### Build/Deploy Failures
- [ ] Check package.json syntax
- [ ] Verify all environment variables set
- [ ] Review build logs in Railway
- [ ] Confirm GitHub repository is accessible

## 💰 Cost Management

### Usage Monitoring
- [ ] Checked initial usage in Railway Metrics
- [ ] Set up usage alerts (optional)
- [ ] Confirmed free tier credits sufficient
- [ ] Added payment method (if planning to scale)

### Optimization
- [ ] Bot only runs necessary processes
- [ ] Health checks use minimal resources
- [ ] No memory leaks in logs
- [ ] Graceful shutdown implemented

## 🔐 Security Final Check

### Credentials Security
- [ ] Bot token never exposed in code/logs
- [ ] Environment variables properly configured
- [ ] `.env` file in `.gitignore`
- [ ] No hardcoded secrets anywhere

### Bot Permissions
- [ ] Bot has minimum required permissions
- [ ] Admin commands properly restricted
- [ ] Error messages don't leak sensitive info
- [ ] Audit logging in place

## ✨ Success Indicators

Your deployment is successful when:
- ✅ Bot shows as **Online** in Discord
- ✅ Health endpoint returns `200 OK`
- ✅ All slash commands work properly
- ✅ Railway shows **Deployed** status
- ✅ No errors in Railway logs
- ✅ Invisible features work as expected

## 🎉 Next Steps

After successful deployment:
- [ ] Document your server setup
- [ ] Train administrators on bot commands
- [ ] Create invisible channels for different purposes
- [ ] Set up regular monitoring routine
- [ ] Plan future feature additions

---

## 📞 Support Resources

- **Railway Support**: [discord.gg/railway](https://discord.gg/railway)
- **Discord.js Docs**: [discord.js.org](https://discord.js.org)
- **Railway Docs**: [docs.railway.app](https://docs.railway.app)
- **Bot Repository**: Check GitHub issues for common problems

**🎯 Pro Tip**: Keep this checklist handy for future deployments or when helping others set up their bots!
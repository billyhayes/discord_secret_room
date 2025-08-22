# Discord Bot Permissions Guide 🤖

A comprehensive guide for setting up Discord bot permissions for your `secret_room#7956` bot.

## 🎯 Quick Start (Recommended)

For most bots, start with these **essential permissions**:

### Basic Bot Setup
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Select your application (`secret_room`)
3. Navigate to **OAuth2 → URL Generator**
4. Select these scopes:
   - ✅ `bot`
   - ✅ `applications.commands`

### Essential Permissions (Check These):
- ✅ **View Channels** - Required to see channels
- ✅ **Send Messages** - Post messages in text channels  
- ✅ **Read Message History** - See previous messages
- ✅ **Embed Links** - Send rich embeds (status reports, etc.)
- ✅ **Use External Emojis** - Use emojis from other servers
- ✅ **Add Reactions** - React to messages
- ✅ **Use Slash Commands** - Modern Discord commands

**Copy the generated URL and use it to add your bot to a server!**

---

## 📋 Permission Categories Explained

### 🔤 Text Channel Permissions
| Permission | Description | When You Need It |
|------------|-------------|------------------|
| **View Channels** | See channel list | ⭐ **Always required** |
| **Send Messages** | Post text messages | ⭐ **Essential for most bots** |
| **Send TTS Messages** | Send text-to-speech messages | Rarely needed |
| **Manage Messages** | Delete/pin messages | Moderation bots |
| **Embed Links** | Send rich embeds | ⭐ **Status reports, fancy messages** |
| **Attach Files** | Upload files/images | Image bots, file sharing |
| **Read Message History** | See old messages | ⭐ **Almost always needed** |
| **Mention Everyone** | Use @everyone/@here | Admin/announcement bots |
| **Use External Emojis** | Use emojis from other servers | ⭐ **Better user experience** |
| **Add Reactions** | React to messages | ⭐ **Interactive features** |
| **Use Slash Commands** | Modern `/command` syntax | ⭐ **Recommended for new bots** |
| **Manage Threads** | Create/edit threads | Thread management |
| **Send Messages in Threads** | Reply in threads | Thread participation |
| **Create Public Threads** | Start public threads | Community features |
| **Create Private Threads** | Start private threads | Moderation/admin features |

### 🔊 Voice Channel Permissions
| Permission | Description | When You Need It |
|------------|-------------|------------------|
| **Connect** | Join voice channels | Music/voice bots |
| **Speak** | Transmit audio | Music/voice bots |
| **Video** | Transmit video | Video bots |
| **Use Voice Activity** | Use voice without push-to-talk | Voice bots |
| **Priority Speaker** | Lower others' volume | Music bots |
| **Mute Members** | Mute users in voice | Moderation |
| **Deafen Members** | Deafen users in voice | Moderation |
| **Move Members** | Move users between channels | Moderation |
| **Use Soundboard** | Use server soundboard | Entertainment bots |

### 👥 Membership Permissions
| Permission | Description | When You Need It |
|------------|-------------|------------------|
| **Change Nickname** | Change bot's nickname | Customization |
| **Manage Nicknames** | Change others' nicknames | Moderation |
| **Kick Members** | Remove users temporarily | Moderation |
| **Ban Members** | Remove users permanently | Moderation |
| **Timeout Members** | Temporarily restrict users | Moderation |

### ⚙️ Advanced Permissions
| Permission | Description | When You Need It |
|------------|-------------|------------------|
| **Manage Channels** | Create/edit channels | Server management |
| **Manage Server** | Edit server settings | Full admin bots |
| **Manage Roles** | Create/assign roles | Role management |
| **Manage Webhooks** | Create webhooks | Integration bots |
| **View Audit Log** | See server audit log | Logging/moderation |
| **View Server Insights** | See analytics | Analytics bots |
| **Manage Emojis and Stickers** | Add custom emojis | Content management |
| **Manage Events** | Create server events | Event bots |
| **Administrator** | ⚠️ **All permissions** | **Use with caution!** |

---

## 🎭 Common Bot Types & Their Permissions

### 🛡️ Moderation Bot
Perfect for server management and keeping things clean.
```
Essential Permissions:
✅ View Channels
✅ Send Messages
✅ Read Message History
✅ Embed Links
✅ Manage Messages (delete spam/inappropriate content)
✅ Kick Members
✅ Ban Members
✅ Timeout Members
✅ Manage Roles (mute role, etc.)
✅ View Audit Log
✅ Use Slash Commands
```

### 🎵 Music Bot
For playing music and managing voice channels.
```
Essential Permissions:
✅ View Channels
✅ Send Messages
✅ Connect (join voice channels)
✅ Speak (play audio)
✅ Use Voice Activity
✅ Embed Links (music info)
✅ Add Reactions (music controls)
✅ Use Slash Commands
✅ Priority Speaker (optional)
```

### 📊 Utility/Status Bot (Like Yours!)
For monitoring, status checks, and helpful commands.
```
Essential Permissions:
✅ View Channels
✅ Send Messages
✅ Read Message History
✅ Embed Links (status reports)
✅ Use External Emojis
✅ Add Reactions
✅ Use Slash Commands
✅ Attach Files (logs, screenshots)
```

### 🎮 Gaming Bot
For game stats, leaderboards, and interactive features.
```
Essential Permissions:
✅ View Channels
✅ Send Messages
✅ Read Message History
✅ Embed Links (game stats)
✅ Attach Files (screenshots)
✅ Use External Emojis
✅ Add Reactions
✅ Manage Messages (game spam cleanup)
✅ Use Slash Commands
```

---

## 🔐 Security Best Practices

### ✅ Do's:
- **Start minimal** - Only request permissions you actually use
- **Add permissions gradually** - As you add features
- **Test in a private server first** - Before public deployment
- **Document what each permission is for** - Help server owners understand
- **Use role-based permissions** - Let servers customize access

### ❌ Don'ts:
- **Never request Administrator** - Unless absolutely necessary
- **Don't request "Manage Server"** - Unless it's a management bot
- **Avoid "Mention Everyone"** - Can be annoying for users
- **Don't request voice permissions** - If you're not using voice features
- **Never store or log sensitive permissions** - Like ban/kick actions unnecessarily

---

## 🚀 Setting Up Your Bot (Step by Step)

### Step 1: Generate Invite URL
1. Visit [Discord Developer Portal](https://discord.com/developers/applications)
2. Click on your `secret_room` application
3. Go to **OAuth2** → **URL Generator**

### Step 2: Select Scopes
```
Required Scopes:
✅ bot
✅ applications.commands (for slash commands)
```

### Step 3: Choose Permissions
For your status/utility bot, select:
```
✅ View Channels
✅ Send Messages  
✅ Read Message History
✅ Embed Links
✅ Use External Emojis
✅ Add Reactions
✅ Use Slash Commands
✅ Attach Files (optional, for logs)
```

### Step 4: Generate and Use URL
1. Copy the generated URL at the bottom
2. Open it in your browser
3. Select a server to add the bot to
4. Click "Authorize"

### Step 5: Test Your Bot
Run your status checker to confirm it's working:
```bash
cd discord
source discord_bot_env/bin/activate
python3 tests/status_check.py
```

---

## 🔧 Permission Troubleshooting

### Common Issues:

**Bot can't send messages:**
- ✅ Check "Send Messages" permission
- ✅ Check channel-specific permissions
- ✅ Ensure bot role is above muted roles

**Embeds not showing:**
- ✅ Enable "Embed Links" permission
- ✅ Check if user has embeds disabled

**Slash commands not working:**
- ✅ Include "applications.commands" scope
- ✅ Re-invite bot with updated permissions
- ✅ Wait up to 1 hour for commands to sync

**Bot seems offline:**
- ✅ Check if bot token is valid
- ✅ Ensure bot is actually running
- ✅ Check "View Channels" permission

---

## 📖 Advanced Configuration

### Channel-Specific Permissions
Remember that server owners can override bot permissions per channel:
- Bot might have "Send Messages" globally but be denied in #announcements
- Always handle permission errors gracefully in your code

### Permission Hierarchy
Discord permissions work in this order:
1. **Server owner** - Always has all permissions
2. **Administrator role** - Bypasses most restrictions  
3. **Role permissions** - Cumulative (multiple roles = more permissions)
4. **Channel overrides** - Can deny or allow specific permissions
5. **Default @everyone role** - Base permissions for all users

### Checking Permissions in Code
```python
# Example: Check if bot can send messages
if ctx.channel.permissions_for(ctx.guild.me).send_messages:
    await ctx.send("I can send messages here!")
else:
    # Handle gracefully - maybe DM user or log error
    print("No permission to send messages in this channel")
```

---

## 🎉 Ready to Go!

Your bot `secret_room#7956` is ready for action! Start with the **essential permissions** listed above, add your bot to a test server, and expand permissions as you add new features.

**Quick Invite URL Generator**: Use the Discord Developer Portal OAuth2 section with the permissions listed in this guide.

Happy botting! 🚀
#!/usr/bin/env python3
"""
Discord Bot OAuth2 URL Generator
Generates invite URLs for your Discord bot with customizable permissions.
"""

import sys
from urllib.parse import urlencode

# Discord OAuth2 base URL
OAUTH_BASE = "https://discord.com/api/oauth2/authorize"

# Permission bit values (Discord API permissions)
PERMISSIONS = {
    # General permissions
    "administrator": 8,
    "view_audit_log": 128,
    "view_server_insights": 524288,
    "manage_server": 32,
    "manage_roles": 268435456,
    "manage_channels": 16,
    "kick_members": 2,
    "ban_members": 4,
    "timeout_members": 1099511627776,
    "create_instant_invite": 1,
    "change_nickname": 67108864,
    "manage_nicknames": 134217728,
    "manage_emojis_and_stickers": 1073741824,
    "manage_webhooks": 536870912,
    "manage_events": 8589934592,

    # Text channel permissions
    "view_channels": 1024,
    "send_messages": 2048,
    "send_tts_messages": 4096,
    "manage_messages": 8192,
    "embed_links": 16384,
    "attach_files": 32768,
    "read_message_history": 65536,
    "mention_everyone": 131072,
    "use_external_emojis": 262144,
    "add_reactions": 64,
    "use_slash_commands": 2147483648,
    "manage_threads": 17179869184,
    "create_public_threads": 34359738368,
    "create_private_threads": 68719476736,
    "send_messages_in_threads": 274877906944,
    "use_external_stickers": 137438953472,

    # Voice channel permissions
    "connect": 1048576,
    "speak": 2097152,
    "mute_members": 4194304,
    "deafen_members": 8388608,
    "move_members": 16777216,
    "use_voice_activity": 33554432,
    "priority_speaker": 256,
    "stream": 512,
    "use_soundboard": 2199023255552,
    "use_external_sounds": 35184372088832,
}

# Pre-defined permission sets
PERMISSION_SETS = {
    "essential": [
        "view_channels", "send_messages", "read_message_history",
        "embed_links", "use_external_emojis", "add_reactions", "use_slash_commands"
    ],

    "utility": [
        "view_channels", "send_messages", "read_message_history",
        "embed_links", "attach_files", "use_external_emojis",
        "add_reactions", "use_slash_commands", "send_messages_in_threads"
    ],

    "moderation": [
        "view_channels", "send_messages", "read_message_history", "embed_links",
        "manage_messages", "kick_members", "ban_members", "timeout_members",
        "manage_roles", "manage_nicknames", "view_audit_log", "use_slash_commands"
    ],

    "music": [
        "view_channels", "send_messages", "connect", "speak", "use_voice_activity",
        "embed_links", "add_reactions", "use_slash_commands", "priority_speaker"
    ],

    "admin": [
        "view_channels", "send_messages", "read_message_history", "embed_links",
        "manage_server", "manage_channels", "manage_roles", "manage_messages",
        "kick_members", "ban_members", "view_audit_log", "use_slash_commands"
    ]
}

def calculate_permissions(permission_list):
    """Calculate the permission integer from a list of permission names"""
    total = 0
    for perm in permission_list:
        if perm in PERMISSIONS:
            total += PERMISSIONS[perm]
        else:
            print(f"⚠️  Warning: Unknown permission '{perm}'")
    return total

def generate_invite_url(client_id, permissions=None, guild_id=None, scopes=None):
    """Generate Discord OAuth2 invite URL"""
    if scopes is None:
        scopes = ["bot", "applications.commands"]

    if permissions is None:
        permissions = 0

    params = {
        "client_id": client_id,
        "permissions": permissions,
        "scope": " ".join(scopes)
    }

    if guild_id:
        params["guild_id"] = guild_id

    return f"{OAUTH_BASE}?{urlencode(params)}"

def print_permission_sets():
    """Display available permission sets"""
    print("📋 Available Permission Sets:")
    print("=" * 50)

    for name, perms in PERMISSION_SETS.items():
        perm_value = calculate_permissions(perms)
        print(f"\n🔹 {name.upper()}:")
        print(f"   Permissions: {perm_value}")
        for perm in perms:
            print(f"   ✅ {perm.replace('_', ' ').title()}")

def print_all_permissions():
    """Display all available permissions"""
    print("🔧 All Available Permissions:")
    print("=" * 50)

    categories = {
        "General": ["administrator", "view_audit_log", "view_server_insights", "manage_server",
                   "manage_roles", "manage_channels", "kick_members", "ban_members", "timeout_members",
                   "create_instant_invite", "change_nickname", "manage_nicknames", "manage_emojis_and_stickers",
                   "manage_webhooks", "manage_events"],

        "Text": ["view_channels", "send_messages", "send_tts_messages", "manage_messages",
                "embed_links", "attach_files", "read_message_history", "mention_everyone",
                "use_external_emojis", "add_reactions", "use_slash_commands", "manage_threads",
                "create_public_threads", "create_private_threads", "send_messages_in_threads",
                "use_external_stickers"],

        "Voice": ["connect", "speak", "mute_members", "deafen_members", "move_members",
                 "use_voice_activity", "priority_speaker", "stream", "use_soundboard", "use_external_sounds"]
    }

    for category, perms in categories.items():
        print(f"\n🔸 {category} Permissions:")
        for perm in perms:
            if perm in PERMISSIONS:
                print(f"   • {perm} ({PERMISSIONS[perm]})")

def interactive_mode():
    """Interactive permission selector"""
    print("🤖 Discord Bot Invite URL Generator")
    print("=" * 50)

    # Get client ID
    client_id = input("\n🆔 Enter your bot's Client ID (from Developer Portal): ").strip()
    if not client_id:
        print("❌ Client ID is required!")
        return None

    # Choose permission method
    print("\n🔧 Choose permission method:")
    print("1. Use pre-defined permission set")
    print("2. Enter custom permissions")
    print("3. Use permission integer directly")

    choice = input("\nEnter choice (1-3): ").strip()

    permissions = 0

    if choice == "1":
        print_permission_sets()
        set_name = input(f"\nChoose a permission set ({'/'.join(PERMISSION_SETS.keys())}): ").strip().lower()
        if set_name in PERMISSION_SETS:
            permissions = calculate_permissions(PERMISSION_SETS[set_name])
            print(f"✅ Using {set_name} permissions: {permissions}")
        else:
            print("❌ Invalid permission set!")
            return None

    elif choice == "2":
        print_all_permissions()
        custom_perms = input("\n📝 Enter permission names (space-separated): ").strip().split()
        permissions = calculate_permissions(custom_perms)
        print(f"✅ Custom permissions calculated: {permissions}")

    elif choice == "3":
        try:
            permissions = int(input("🔢 Enter permission integer: ").strip())
            print(f"✅ Using permission integer: {permissions}")
        except ValueError:
            print("❌ Invalid number!")
            return None
    else:
        print("❌ Invalid choice!")
        return None

    # Optional guild ID
    guild_id = input("\n🏠 Enter Guild/Server ID (optional, press Enter to skip): ").strip()
    if guild_id == "":
        guild_id = None

    # Generate URL
    url = generate_invite_url(client_id, permissions, guild_id)

    print("\n" + "=" * 60)
    print("🎉 Generated Invite URL:")
    print("=" * 60)
    print(url)
    print("=" * 60)

    print("\n📋 Instructions:")
    print("1. Copy the URL above")
    print("2. Open it in your web browser")
    print("3. Select a server to add the bot to")
    print("4. Click 'Authorize'")
    print("5. Your bot will be added with the specified permissions!")

    return url

def main():
    """Main function"""
    if len(sys.argv) == 1:
        # Interactive mode
        interactive_mode()
    elif len(sys.argv) >= 3:
        # Command line mode
        client_id = sys.argv[1]

        if sys.argv[2].isdigit():
            # Permission integer provided
            permissions = int(sys.argv[2])
        elif sys.argv[2] in PERMISSION_SETS:
            # Permission set name provided
            permissions = calculate_permissions(PERMISSION_SETS[sys.argv[2]])
        else:
            # Custom permission list
            custom_perms = sys.argv[2:]
            permissions = calculate_permissions(custom_perms)

        url = generate_invite_url(client_id, permissions)
        print("🔗 Generated URL:")
        print(url)
    else:
        # Help message
        print("🤖 Discord Bot OAuth2 URL Generator")
        print("=" * 50)
        print("\nUsage:")
        print("  Interactive mode:")
        print("    python3 generate_invite.py")
        print("\n  Command line mode:")
        print("    python3 generate_invite.py <CLIENT_ID> <PERMISSIONS>")
        print("    python3 generate_invite.py <CLIENT_ID> <PERMISSION_SET>")
        print("    python3 generate_invite.py <CLIENT_ID> <PERM1> <PERM2> ...")
        print("\nExamples:")
        print("    python3 generate_invite.py 123456789 essential")
        print("    python3 generate_invite.py 123456789 2048")
        print("    python3 generate_invite.py 123456789 view_channels send_messages")
        print("\nAvailable permission sets:")
        for name in PERMISSION_SETS.keys():
            print(f"    • {name}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"💥 Error: {e}")
        sys.exit(1)

#!/usr/bin/env python3
"""
Discord Permission Decoder
Decodes Discord permission integers into human-readable permission lists.
"""

# Discord permission bit values
PERMISSIONS = {
    1: "create_instant_invite",
    2: "kick_members",
    4: "ban_members",
    8: "administrator",
    16: "manage_channels",
    32: "manage_server",
    64: "add_reactions",
    128: "view_audit_log",
    256: "priority_speaker",
    512: "stream",
    1024: "view_channels",
    2048: "send_messages",
    4096: "send_tts_messages",
    8192: "manage_messages",
    16384: "embed_links",
    32768: "attach_files",
    65536: "read_message_history",
    131072: "mention_everyone",
    262144: "use_external_emojis",
    524288: "view_server_insights",
    1048576: "connect",
    2097152: "speak",
    4194304: "mute_members",
    8388608: "deafen_members",
    16777216: "move_members",
    33554432: "use_voice_activity",
    67108864: "change_nickname",
    134217728: "manage_nicknames",
    268435456: "manage_roles",
    536870912: "manage_webhooks",
    1073741824: "manage_emojis_and_stickers",
    2147483648: "use_slash_commands",
    4294967296: "request_to_speak",
    8589934592: "manage_events",
    17179869184: "manage_threads",
    34359738368: "create_public_threads",
    68719476736: "create_private_threads",
    137438953472: "use_external_stickers",
    274877906944: "send_messages_in_threads",
    549755813888: "use_embedded_activities",
    1099511627776: "timeout_members",
    2199023255552: "use_soundboard",
    4398046511104: "create_expressions",
    8796093022208: "use_external_sounds",
    17592186044416: "send_voice_messages"
}

# Permission categories for better organization
CATEGORIES = {
    "General": [
        "administrator", "manage_server", "manage_roles", "manage_channels",
        "kick_members", "ban_members", "timeout_members", "create_instant_invite",
        "change_nickname", "manage_nicknames", "view_audit_log", "view_server_insights",
        "manage_webhooks", "manage_events", "manage_emojis_and_stickers"
    ],
    "Text": [
        "view_channels", "send_messages", "send_tts_messages", "manage_messages",
        "embed_links", "attach_files", "read_message_history", "mention_everyone",
        "use_external_emojis", "add_reactions", "use_slash_commands", "manage_threads",
        "create_public_threads", "create_private_threads", "send_messages_in_threads",
        "use_external_stickers", "send_voice_messages"
    ],
    "Voice": [
        "connect", "speak", "mute_members", "deafen_members", "move_members",
        "use_voice_activity", "priority_speaker", "stream", "request_to_speak",
        "use_soundboard", "use_external_sounds", "use_embedded_activities"
    ],
    "Special": [
        "create_expressions"
    ]
}

def decode_permissions(permission_int):
    """Decode a permission integer into a list of permission names"""
    permissions = []

    for bit_value, perm_name in PERMISSIONS.items():
        if permission_int & bit_value:
            permissions.append(perm_name)

    return permissions

def format_permissions_by_category(permissions):
    """Group permissions by category for better display"""
    categorized = {}

    for category, category_perms in CATEGORIES.items():
        found_perms = [p for p in permissions if p in category_perms]
        if found_perms:
            categorized[category] = found_perms

    # Handle any permissions not in categories
    all_categorized = []
    for category_perms in CATEGORIES.values():
        all_categorized.extend(category_perms)

    uncategorized = [p for p in permissions if p not in all_categorized]
    if uncategorized:
        categorized["Other"] = uncategorized

    return categorized

def print_decoded_permissions(permission_int):
    """Print a formatted breakdown of permissions"""
    print(f"🔢 Permission Integer: {permission_int}")
    print("=" * 60)

    permissions = decode_permissions(permission_int)

    if not permissions:
        print("❌ No permissions found (or invalid permission integer)")
        return

    print(f"✅ Total Permissions: {len(permissions)}")
    print()

    # Group by category
    categorized = format_permissions_by_category(permissions)

    for category, perms in categorized.items():
        icon = "🛡️" if category == "General" else "💬" if category == "Text" else "🔊" if category == "Voice" else "⭐"
        print(f"{icon} {category} Permissions ({len(perms)}):")

        for perm in sorted(perms):
            # Format permission name for display
            display_name = perm.replace("_", " ").title()
            bit_value = next((k for k, v in PERMISSIONS.items() if v == perm), None)
            print(f"   ✅ {display_name} (bit: {bit_value})")
        print()

    # Show danger level
    danger_level = get_danger_level(permissions)
    print(f"⚠️  Permission Risk Level: {danger_level}")

    # Show summary
    print("\n📋 Summary:")
    if "administrator" in permissions:
        print("   🚨 ADMINISTRATOR - Bot has ALL permissions!")
    else:
        can_moderate = any(p in permissions for p in ["kick_members", "ban_members", "manage_messages", "timeout_members"])
        can_manage = any(p in permissions for p in ["manage_server", "manage_channels", "manage_roles"])
        can_voice = any(p in permissions for p in ["connect", "speak", "mute_members"])

        if can_manage:
            print("   🔧 Can manage server/channels/roles")
        if can_moderate:
            print("   🛡️ Has moderation capabilities")
        if can_voice:
            print("   🔊 Has voice channel access")
        if not (can_manage or can_moderate or can_voice):
            print("   📝 Basic utility bot permissions")

def get_danger_level(permissions):
    """Assess the risk level of the permission set"""
    if "administrator" in permissions:
        return "🔴 CRITICAL - Full admin access"

    high_risk = ["manage_server", "manage_roles", "ban_members", "manage_webhooks"]
    medium_risk = ["kick_members", "manage_messages", "manage_channels", "timeout_members"]

    high_count = sum(1 for p in permissions if p in high_risk)
    medium_count = sum(1 for p in permissions if p in medium_risk)

    if high_count >= 2:
        return "🟠 HIGH - Multiple dangerous permissions"
    elif high_count >= 1:
        return "🟡 MEDIUM - Some risky permissions"
    elif medium_count >= 2:
        return "🟡 MEDIUM - Multiple moderation permissions"
    else:
        return "🟢 LOW - Safe permission set"

def compare_permissions(perm1, perm2):
    """Compare two permission integers"""
    perms1 = set(decode_permissions(perm1))
    perms2 = set(decode_permissions(perm2))

    print(f"🔍 Comparing Permissions")
    print("=" * 40)
    print(f"Permission Set 1: {perm1}")
    print(f"Permission Set 2: {perm2}")
    print()

    # Find differences
    only_in_1 = perms1 - perms2
    only_in_2 = perms2 - perms1
    common = perms1 & perms2

    if common:
        print(f"✅ Common Permissions ({len(common)}):")
        for perm in sorted(common):
            print(f"   • {perm.replace('_', ' ').title()}")
        print()

    if only_in_1:
        print(f"🔵 Only in Set 1 ({len(only_in_1)}):")
        for perm in sorted(only_in_1):
            print(f"   + {perm.replace('_', ' ').title()}")
        print()

    if only_in_2:
        print(f"🟠 Only in Set 2 ({len(only_in_2)}):")
        for perm in sorted(only_in_2):
            print(f"   + {perm.replace('_', ' ').title()}")
        print()

def main():
    """Main function with CLI interface"""
    import sys

    if len(sys.argv) < 2:
        print("🔍 Discord Permission Decoder")
        print("=" * 40)
        print("Usage:")
        print("  python3 decode_permissions.py <permission_integer>")
        print("  python3 decode_permissions.py <perm1> <perm2>  (compare)")
        print()
        print("Examples:")
        print("  python3 decode_permissions.py 2048")
        print("  python3 decode_permissions.py 3971431638498551")
        print("  python3 decode_permissions.py 2048 8192")
        return

    try:
        perm1 = int(sys.argv[1])

        if len(sys.argv) == 3:
            # Compare mode
            perm2 = int(sys.argv[2])
            compare_permissions(perm1, perm2)
        else:
            # Single permission decode
            print_decoded_permissions(perm1)

    except ValueError:
        print("❌ Error: Please provide valid integers")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()

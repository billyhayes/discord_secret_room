#!/bin/bash

# Discord Bot Environment Activation Script
# This script activates the virtual environment and provides helpful information

echo "🤖 Discord Bot Development Environment"
echo "======================================"

# Check if virtual environment exists
if [ ! -d "discord_bot_env" ]; then
    echo "❌ Virtual environment not found!"
    echo "📋 Creating virtual environment..."
    python3 -m venv discord_bot_env

    if [ $? -eq 0 ]; then
        echo "✅ Virtual environment created successfully!"
    else
        echo "❌ Failed to create virtual environment"
        exit 1
    fi
fi

# Activate the virtual environment
echo "🔄 Activating virtual environment..."
source discord_bot_env/bin/activate

# Check if discord.py is installed
if python3 -c "import discord" 2>/dev/null; then
    echo "✅ discord.py is installed"
    python3 -c "import discord; print(f'📦 Discord.py version: {discord.__version__}')"
else
    echo "⚠️  discord.py not found, installing..."
    pip install discord.py
fi

echo ""
echo "🎉 Environment is ready!"
echo ""
echo "📂 Available scripts:"
echo "  • python3 tests/bot_status.py - Bot status checker"
echo ""
echo "💡 Useful commands:"
echo "  • deactivate - Exit virtual environment"
echo "  • pip list - Show installed packages"
echo "  • python3 --version - Check Python version"
echo ""
echo "🔧 To run the bot status checker:"
echo "  1. Edit tests/bot_status.py and add your bot token"
echo "  2. Uncomment one of the test options"
echo "  3. Run: python3 tests/bot_status.py"
echo ""

#!/bin/bash
#
# Moose Music Player - One-Click Launcher
# This script starts everything automatically
#

cd "$(dirname "$0")"

echo "🎵 Moose Music Player"
echo "====================="
echo ""

# Check dependencies
if ! command -v ngrok &> /dev/null; then
    echo "❌ ngrok not found. Installing..."
    brew install ngrok
    echo "⚠️  Please run: ngrok config add-authtoken YOUR_TOKEN"
    echo "Get token from: https://dashboard.ngrok.com/get-started/your-authtoken"
    exit 1
fi

echo "✅ ngrok found"

# Start Python launcher
echo "🚀 Starting auto-launcher..."
python3 auto-launch.py

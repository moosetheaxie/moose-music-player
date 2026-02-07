#!/bin/bash

echo "🎵 Moose Music Player - Launcher"
echo "================================="
echo ""

# Check if ngrok is installed
if ! command -v ngrok &> /dev/null; then
    echo "❌ ngrok not found. Installing..."
    brew install ngrok
    echo "⚠️  You'll need to configure ngrok with your authtoken:"
    echo "   ngrok config add-authtoken YOUR_TOKEN"
    echo ""
    echo "Get your token from: https://dashboard.ngrok.com/get-started/your-authtoken"
    exit 1
fi

# Start the music server in background
echo "🚀 Starting music server..."
cd ~/.openclaw/workspace/music_player
python3 server.py &
SERVER_PID=$!

# Wait for server to start
sleep 2

echo "🌐 Starting ngrok tunnel..."
echo ""
echo "📱 Open the web UI and paste the ngrok HTTPS URL"
echo ""

# Start ngrok
ngrok http 5000

# When ngrok exits, kill the server
echo ""
echo "🛑 Stopping music server..."
kill $SERVER_PID 2>/dev/null

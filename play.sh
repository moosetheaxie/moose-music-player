#!/bin/bash
# 🎵 Moose Music Player - ULTIMATE ONE-CLICK
# Everything in one script

cd "$(dirname "$0")"

echo "🎵 Moose Music Player"
echo "====================="
echo ""

# Check if server is running
if ! curl -s http://localhost:8080/status >/dev/null 2>&1; then
    echo "🚀 Starting music server..."
    launchctl start com.moose.musicplayer 2>/dev/null || python3 ../music_player/server.py &
    sleep 2
fi

echo "✅ Music server running"

# Check for ngrok
if ! command -v ngrok &> /dev/null; then
    echo "❌ ngrok not found. Install with: brew install ngrok"
    echo "   Then: ngrok config add-authtoken YOUR_TOKEN"
    exit 1
fi

echo "🌐 Starting tunnel..."
echo ""

# Start ngrok and capture URL
ngrok http 5000 --log=stdout &
NGROK_PID=$!

# Wait for ngrok to start
sleep 4

# Get the ngrok URL
TUNNEL_URL=$(curl -s http://localhost:4040/api/tunnels | python3 -c "import sys, json; d=json.load(sys.stdin); print([t['public_url'] for t in d['tunnels'] if t['proto']=='https'][0])" 2>/dev/null)

if [ -n "$TUNNEL_URL" ]; then
    echo ""
    echo "========================================"
    echo "🚀 BACKEND URL: $TUNNEL_URL"
    echo "========================================"
    echo ""
    
    # Open web UI with URL parameter
    WEB_URL="https://moose-music-player.vercel.app/?backend=${TUNNEL_URL#https://}"
    open "$WEB_URL"
    
    echo "📱 Web UI opened in browser!"
    echo ""
    echo "🛑 Press Ctrl+C to stop tunnel"
    echo "   (Music server keeps running)"
else
    echo "⚠️  Tunnel starting... wait a moment"
fi

# Wait for interrupt
trap "echo ''; echo '🛑 Stopping...'; kill $NGROK_PID 2>/dev/null; exit 0" INT
wait $NGROK_PID

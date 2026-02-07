#!/bin/bash
# 🎵 Moose Music Player - ONE CLICK (auto backend)

set -euo pipefail
cd "$(dirname "$0")"

WEB_URL="https://moose-music-player.vercel.app"

echo "🎵 Moose Music Player"
echo "====================="

if ! curl -s http://localhost:8080/status >/dev/null 2>&1; then
  echo "🚀 Starting music server..."
  launchctl start com.moose.musicplayer 2>/dev/null || python3 ../music_player/server.py &
  sleep 2
fi

echo "✅ Music server running"

launchctl start com.moose.musicplayer.tunnel >/dev/null 2>&1 || true
sleep 3

BACKEND_URL=$(curl -s http://127.0.0.1:4040/api/tunnels | python3 -c "import sys,json; d=json.load(sys.stdin); print([t['public_url'] for t in d.get('tunnels',[]) if t.get('proto')=='https'][0])" 2>/dev/null || true)

if [ -n "$BACKEND_URL" ]; then
  echo "🌐 Backend URL: $BACKEND_URL"
  open "$WEB_URL/?backend=${BACKEND_URL#https://}"
else
  echo "⚠️ Could not detect tunnel URL; opening app anyway"
  open "$WEB_URL"
fi

echo "Done."

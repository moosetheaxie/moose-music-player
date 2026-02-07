#!/bin/bash
# Install Moose Music Player as a system service

echo "🎵 Installing Moose Music Player Auto-Start..."

# Copy plists to LaunchAgents
PLIST_SERVER_SOURCE="/Users/moose/.openclaw/workspace/music-player-web/com.moose.musicplayer.plist"
PLIST_SERVER_DEST="$HOME/Library/LaunchAgents/com.moose.musicplayer.plist"
PLIST_TUNNEL_SOURCE="/Users/moose/.openclaw/workspace/music-player-web/com.moose.musicplayer.tunnel.plist"
PLIST_TUNNEL_DEST="$HOME/Library/LaunchAgents/com.moose.musicplayer.tunnel.plist"

cp "$PLIST_SERVER_SOURCE" "$PLIST_SERVER_DEST"
cp "$PLIST_TUNNEL_SOURCE" "$PLIST_TUNNEL_DEST"

# Load services (reload-safe)
launchctl unload "$PLIST_SERVER_DEST" >/dev/null 2>&1 || true
launchctl unload "$PLIST_TUNNEL_DEST" >/dev/null 2>&1 || true
launchctl load "$PLIST_SERVER_DEST"
launchctl load "$PLIST_TUNNEL_DEST"

# Start services
launchctl start com.moose.musicplayer
launchctl start com.moose.musicplayer.tunnel

echo "✅ Music server + tunnel will auto-start on login!"
echo ""
echo "If you set a reserved ngrok domain, backend URL will be fully persistent."
echo "To check status: launchctl list | grep moose"
echo "To stop server: launchctl stop com.moose.musicplayer"
echo "To stop tunnel: launchctl stop com.moose.musicplayer.tunnel"
echo "To uninstall: launchctl unload $PLIST_SERVER_DEST && launchctl unload $PLIST_TUNNEL_DEST"

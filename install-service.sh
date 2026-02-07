#!/bin/bash
# Install Moose Music Player as a system service

echo "🎵 Installing Moose Music Player Auto-Start..."

# Copy plist to LaunchAgents
PLIST_SOURCE="/Users/moose/.openclaw/workspace/music-player-web/com.moose.musicplayer.plist"
PLIST_DEST="$HOME/Library/LaunchAgents/com.moose.musicplayer.plist"

cp "$PLIST_SOURCE" "$PLIST_DEST"

# Load the service
launchctl load "$PLIST_DEST"

# Start the service
launchctl start com.moose.musicplayer

echo "✅ Music server will auto-start on login!"
echo ""
echo "To check status: launchctl list | grep moose"
echo "To stop: launchctl stop com.moose.musicplayer"
echo "To uninstall: launchctl unload $PLIST_DEST"

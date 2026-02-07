#!/usr/bin/env python3
"""
Moose Music Player - Easy Launcher
Starts local server and opens web UI
"""

import subprocess
import time
import webbrowser
import sys

def main():
    print("🎵 Moose Music Player")
    print("=" * 40)
    print()
    
    # Check for ngrok
    try:
        subprocess.run(['ngrok', 'version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ ngrok not found. Install with: brew install ngrok")
        print("   Then add your authtoken: ngrok config add-authtoken YOUR_TOKEN")
        sys.exit(1)
    
    print("✅ ngrok found")
    print()
    print("🚀 Starting music server on http://localhost:8080...")
    print()
    
    # Start the server
    server_process = subprocess.Popen(
        ['python3', 'server.py'],
        cwd='/Users/moose/.openclaw/workspace/music_player',
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    
    # Wait for server to start
    time.sleep(2)
    
    print("✅ Music server running")
    print()
    print("🌐 Starting ngrok tunnel...")
    print("   (Copy the HTTPS URL when it appears)")
    print()
    print("📱 Web UI will be available at:")
    print("   [Vercel URL - deploying...]")
    print()
    print("⚠️  Press Ctrl+C to stop")
    print()
    
    try:
        # Start ngrok
        subprocess.run(['ngrok', 'http', '5000'], check=True)
    except KeyboardInterrupt:
        print("\n🛑 Stopping...")
    finally:
        server_process.terminate()
        print("✅ Server stopped")

if __name__ == '__main__':
    main()

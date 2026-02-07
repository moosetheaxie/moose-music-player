#!/usr/bin/env python3
"""
Moose Music Player - Persistent Tunnel
Uses localtunnel for a consistent URL
"""

import subprocess
import time
import json
import urllib.request
import os
import sys

TUNNEL_URL_FILE = "/tmp/moose-music-url.txt"

def get_existing_tunnel():
    """Check if we already have a tunnel running"""
    try:
        with open(TUNNEL_URL_FILE, 'r') as f:
            return f.read().strip()
    except:
        return None

def save_tunnel_url(url):
    """Save tunnel URL to file"""
    with open(TUNNEL_URL_FILE, 'w') as f:
        f.write(url)

def start_tunnel():
    """Start localtunnel"""
    print("🌐 Starting tunnel...")
    
    # Try localtunnel first (free, consistent URLs)
    try:
        proc = subprocess.Popen(
            ['npx', 'localtunnel', '--port', '5000', '--subdomain', 'moose-music-' + os.environ.get('USER', 'user')],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        time.sleep(3)
        
        # Get URL from localtunnel
        try:
            response = urllib.request.urlopen('http://localhost:8080')
            # Localtunnel prints URL to stderr
            return proc
        except:
            pass
    except:
        pass
    
    # Fallback to ngrok
    print("Using ngrok fallback...")
    proc = subprocess.Popen(
        ['ngrok', 'http', '5000'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return proc

def get_tunnel_url():
    """Get tunnel URL from ngrok API"""
    try:
        response = urllib.request.urlopen('http://localhost:4040/api/tunnels')
        data = json.loads(response.read())
        for tunnel in data['tunnels']:
            if tunnel['proto'] == 'https':
                return tunnel['public_url']
    except:
        pass
    return None

def main():
    # Check if server is running
    try:
        urllib.request.urlopen('http://localhost:8080', timeout=2)
        print("✅ Music server is running")
    except:
        print("❌ Music server not running. Start it first with:")
        print("   launchctl start com.moose.musicplayer")
        sys.exit(1)
    
    # Check existing tunnel
    existing = get_existing_tunnel()
    if existing:
        print(f"🌐 Existing tunnel: {existing}")
        print("If not working, delete /tmp/moose-music-url.txt and restart")
        return
    
    # Start new tunnel
    proc = start_tunnel()
    time.sleep(3)
    
    # Get URL
    url = get_tunnel_url()
    if url:
        save_tunnel_url(url)
        print(f"\n{'='*60}")
        print(f"🚀 TUNNEL URL: {url}")
        print(f"{'='*60}")
        print(f"\n📱 Web UI: https://moose-music-player-k1trcbecd-mooses-projects-082601d3.vercel.app")
        print(f"⚙️  Paste this backend URL: {url}")
        print(f"\n🛑 Press Ctrl+C to stop tunnel")
        print(f"   (Server keeps running!)")
        
        try:
            proc.wait()
        except KeyboardInterrupt:
            print("\n🛑 Stopping tunnel...")
            proc.terminate()
    else:
        print("❌ Could not get tunnel URL")
        proc.terminate()

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Moose Music Player - Auto Launcher
Starts server + ngrok and provides easy access to the tunnel URL
"""

import subprocess
import time
import json
import urllib.request
import os
import signal
import sys
from threading import Thread

class MusicLauncher:
    def __init__(self):
        self.server_process = None
        self.ngrok_process = None
        self.ngrok_url = None
        
    def start_server(self):
        """Start the music player server"""
        print("🎵 Starting Music Server...")
        self.server_process = subprocess.Popen(
            ['python3', 'server.py'],
            cwd='/Users/moose/.openclaw/workspace/music_player',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        time.sleep(2)
        print("✅ Server running on http://localhost:5000")
        
    def start_ngrok(self):
        """Start ngrok tunnel"""
        print("🌐 Starting ngrok tunnel...")
        self.ngrok_process = subprocess.Popen(
            ['ngrok', 'http', '5000', '--log=stdout'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Wait for ngrok to start and get URL
        time.sleep(3)
        self.get_ngrok_url()
        
    def get_ngrok_url(self):
        """Get the ngrok tunnel URL from the API"""
        try:
            # Try to get URL from ngrok API
            response = urllib.request.urlopen('http://localhost:4040/api/tunnels')
            data = json.loads(response.read())
            
            for tunnel in data['tunnels']:
                if tunnel['proto'] == 'https':
                    self.ngrok_url = tunnel['public_url']
                    break
                    
            if self.ngrok_url:
                print(f"\n{'='*60}")
                print(f"🚀 NGROK URL: {self.ngrok_url}")
                print(f"{'='*60}\n")
                self.create_quick_access_page()
                return True
        except:
            pass
        return False
        
    def create_quick_access_page(self):
        """Create a local HTML page with the current URL"""
        if not self.ngrok_url:
            return
            
        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0;url=https://moose-music-player-k1trcbecd-mooses-projects-082601d3.vercel.app/?backend={self.ngrok_url.replace('https://', '')}">
    <title>Moose Music Player</title>
    <style>
        body {{
            font-family: -apple-system, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: white;
            text-align: center;
        }}
        .container {{
            background: rgba(255,255,255,0.1);
            padding: 40px;
            border-radius: 20px;
        }}
        h1 {{ margin-bottom: 20px; }}
        .url {{
            background: rgba(255,255,255,0.2);
            padding: 15px;
            border-radius: 10px;
            font-family: monospace;
            margin: 20px 0;
            word-break: break-all;
        }}
        a {{
            color: #667eea;
            text-decoration: none;
            font-size: 18px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🎵 Moose Music Player</h1>
        <p>Opening web player with your backend...</p>
        <div class="url">{self.ngrok_url}</div>
        <p>If not redirected automatically:</p>
        <p><a href="https://moose-music-player-k1trcbecd-mooses-projects-082601d3.vercel.app/?backend={self.ngrok_url.replace('https://', '')}">Click here to open</a></p>
    </div>
</body>
</html>"""
        
        # Save to a file that opens in browser
        quick_access_path = '/Users/moose/.openclaw/workspace/music-player-web/quick-access.html'
        with open(quick_access_path, 'w') as f:
            f.write(html)
            
        # Open it in browser
        subprocess.run(['open', quick_access_path])
        print(f"📱 Quick access page opened in browser")
        
    def show_qr_code(self):
        """Show QR code for easy mobile access"""
        if self.ngrok_url:
            print(f"\n📱 Scan this URL on your phone:")
            print(f"   {self.ngrok_url}")
            print(f"\n🌐 Or open:")
            print(f"   https://moose-music-player-k1trcbecd-mooses-projects-082601d3.vercel.app")
            print(f"\n⚙️  Backend URL to paste: {self.ngrok_url}")
            
    def monitor(self):
        """Monitor processes and show status"""
        print("\n" + "="*60)
        print("🎵 Moose Music Player is RUNNING!")
        print("="*60)
        print(f"\n🖥️  Local Server: http://localhost:5000")
        if self.ngrok_url:
            print(f"🌐 Public URL:   {self.ngrok_url}")
        print(f"\n🌐 Web UI:       https://moose-music-player-k1trcbecd-mooses-projects-082601d3.vercel.app")
        print("\n⚡ Quick Play Commands:")
        print("   ./play.sh '410 Sidhu Moosewala'")
        print("   ./play.sh 'Old School'")
        print("   ./stop.sh")
        print("\n🛑 Press Ctrl+C to stop")
        print("="*60 + "\n")
        
        try:
            while True:
                time.sleep(1)
                # Check if processes are still running
                if self.server_process.poll() is not None:
                    print("❌ Server stopped unexpectedly")
                    break
                if self.ngrok_process.poll() is not None:
                    print("❌ ngrok stopped unexpectedly")
                    break
        except KeyboardInterrupt:
            print("\n\n🛑 Stopping...")
            
    def stop(self):
        """Stop all processes"""
        if self.ngrok_process:
            self.ngrok_process.terminate()
        if self.server_process:
            self.server_process.terminate()
        print("✅ Stopped")
        
    def run(self):
        """Main run loop"""
        try:
            self.start_server()
            self.start_ngrok()
            
            # Try to get URL again if first attempt failed
            if not self.ngrok_url:
                time.sleep(2)
                self.get_ngrok_url()
                
            self.show_qr_code()
            self.monitor()
        finally:
            self.stop()

def main():
    launcher = MusicLauncher()
    launcher.run()

if __name__ == '__main__':
    main()

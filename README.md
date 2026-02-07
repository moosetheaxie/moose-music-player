# 🎵 Moose Music Player - Fully Automated

Control your Mac's music (through WILLEN speaker) from any device on your network!

## ✨ What You Get

- **Web UI** deployed on Vercel (publicly accessible)
- **Auto tunnel** via ngrok (no manual URL copying!)
- **One-click start** - everything launches automatically
- **Auto-connect** - web UI connects to your Mac automatically

---

## 🚀 Quick Start (First Time Setup)

### 1. Install ngrok (if not already installed)
```bash
brew install ngrok
ngrok config add-authtoken YOUR_TOKEN
```
Get your token: https://dashboard.ngrok.com/get-started/your-authtoken

### 2. Start Everything
```bash
cd ~/.openclaw/workspace/music-player-web
./start.sh
```

That's it! The script will:
- ✅ Start the music server on your Mac
- ✅ Create ngrok tunnel
- ✅ Open browser with auto-connected web UI
- ✅ Show you the public URL

---

## 📱 How to Use

### From Your Phone:
1. Open the Vercel URL: **https://moose-music-player-k1trcbecd-mooses-projects-082601d3.vercel.app**
2. Paste the ngrok URL shown in your terminal (or it auto-connects if you opened via start.sh)
3. Search songs or click quick-play buttons
4. Audio plays through **WILLEN** speaker!

### Quick Terminal Commands:
```bash
# While server is running:
./play.sh "410 Sidhu Moosewala"   # Play a song
./stop.sh                          # Stop playback
```

---

## 🔧 Manual Mode (If Auto Fails)

### Start server:
```bash
cd ~/.openclaw/workspace/music_player
python3 server.py
```

### Start ngrok (in another terminal):
```bash
ngrok http 5000
```

### Copy the HTTPS URL and paste into web UI.

---

## 📁 Files

| File | Purpose |
|------|---------|
| `start.sh` | One-click launcher (use this!) |
| `auto-launch.py` | Python script that manages everything |
| `play.sh` | Quick play command |
| `stop.sh` | Quick stop command |
| `index.html` | Web UI (also deployed to Vercel) |

---

## 🎯 Features

- **Quick Play Buttons**: 410, Old School, Rehle Mere Kol, For A Reason
- **Volume Control**: Slider adjusts Mac system volume
- **Search**: Type any song name and press Enter
- **Auto-reconnect**: URL saved in browser

---

## 🛑 Stopping

Press `Ctrl+C` in the terminal running start.sh - it stops both server and ngrok.

---

## 🔗 URLs

- **Web UI**: https://moose-music-player-k1trcbecd-mooses-projects-082601d3.vercel.app
- **Local Server**: http://localhost:5000 (when running)
- **Project Folder**: `~/.openclaw/workspace/music-player-web/`

Enjoy your music! 🎵

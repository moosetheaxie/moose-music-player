# 🎵 Moose Music Player - ZERO CONFIG

**Just click song names. That's it.**

## 🚀 Super Quick Start

### ONE-TIME SETUP (2 minutes):
```bash
cd ~/.openclaw/workspace/music-player-web
./install-service.sh
```

This installs the music server to auto-start on login.

### DAILY USAGE - Option 1: Desktop App
```bash
./desktop.py
```
Click song buttons. Music plays on WILLEN.

### DAILY USAGE - Option 2: Web UI (Phone/Any Device)
```bash
./play.sh
```
This:
1. ✅ Starts ngrok tunnel
2. ✅ Opens browser with auto-connected web UI
3. ✅ Just click songs on your phone!

**Web URL:** https://moose-music-player-k1trcbecd-mooses-projects-082601d3.vercel.app

---

## 🎯 Three Ways to Play

| Method | Command | Best For |
|--------|---------|----------|
| **Desktop App** | `./desktop.py` | Quick control from Mac |
| **Web + Tunnel** | `./play.sh` | Phone/tablet control |
| **Web Manual** | Open Vercel URL | When tunnel is already running |

---

## 📱 Mobile Control

1. Run `./play.sh` on your Mac
2. It opens the web UI in your browser
3. **Bookmark the page** on your phone
4. Now just open the bookmark anytime!

The ngrok URL changes each session, but the web UI auto-updates.

---

## 🔧 Commands

```bash
./install-service.sh     # Install auto-start (run once)
./desktop.py            # Desktop app with buttons
./play.sh               # Start tunnel + open web UI
./stop.sh               # Stop playback
launchctl stop com.moose.musicplayer  # Stop server completely
```

---

## 🎵 Quick Play Songs

- **410** (Sidhu Moosewala)
- **Old School** (Sidhu Moosewala)
- **Rehle Mere Kol**
- **For A Reason** (Karan Aujla)
- **These Days** (Sidhu Moosewala)
- **Legend** (Sidhu Moosewala)

---

## 🌐 URLs

- **Web UI**: https://moose-music-player-k1trcbecd-mooses-projects-082601d3.vercel.app
- **Local Server**: http://localhost:5000

---

## ✅ What's Automated?

- ✅ Music server starts on Mac boot
- ✅ One script starts tunnel + opens browser
- ✅ Web UI auto-connects to your Mac
- ✅ Click song = instant play on WILLEN

**You literally just click song names. Done.**

#!/usr/bin/env python3
"""
Moose Music Player - Desktop Controller
Simple Mac app with song buttons
"""

import tkinter as tk
from tkinter import ttk
import subprocess
import requests
import webbrowser
import os

BACKEND_URL = "http://localhost:8080"

def play_song(song_name):
    """Play a song"""
    try:
        response = requests.post(f"{BACKEND_URL}/play", 
                               json={"song": song_name},
                               timeout=5)
        if response.json().get('success'):
            status_label.config(text=f"▶️ Playing: {song_name}")
        else:
            status_label.config(text="❌ Error playing song")
    except:
        status_label.config(text="❌ Server not running. Run ./start.sh first")

def stop_music():
    """Stop music"""
    try:
        requests.post(f"{BACKEND_URL}/stop", timeout=5)
        status_label.config(text="⏹ Stopped")
    except:
        pass

def open_web():
    """Open web UI"""
    webbrowser.open("https://moose-music-player-k1trcbecd-mooses-projects-082601d3.vercel.app")

def set_volume(val):
    """Set volume"""
    try:
        requests.post(f"{BACKEND_URL}/volume", 
                     json={"volume": int(val)},
                     timeout=5)
    except:
        pass

# Create main window
root = tk.Tk()
root.title("🎵 Moose Music")
root.geometry("350x500")
root.configure(bg='#1a1a2e')

# Style
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=10)

# Title
title = tk.Label(root, text="🦔 Moose Music", 
                font=('Helvetica', 20, 'bold'),
                bg='#1a1a2e', fg='white')
title.pack(pady=20)

# Quick play buttons
songs = [
    ("410", "410 Sidhu Moosewala"),
    ("Old School", "Old School Sidhu Moosewala"),
    ("Rehle Mere Kol", "Rehle Mere Kol"),
    ("For A Reason", "For A Reason Karan Aujla"),
    ("These Days", "These Days Sidhu Moosewala"),
    ("Legend", "Legend Sidhu Moosewala"),
]

btn_frame = tk.Frame(root, bg='#1a1a2e')
btn_frame.pack(pady=10)

for short_name, full_name in songs:
    btn = tk.Button(btn_frame, text=short_name,
                   command=lambda n=full_name: play_song(n),
                   bg='#667eea', fg='white',
                   font=('Helvetica', 11),
                   width=20, height=2,
                   relief='flat', cursor='hand2')
    btn.pack(pady=5)
    btn.bind('<Enter>', lambda e, b=btn: b.config(bg='#764ba2'))
    btn.bind('<Leave>', lambda e, b=btn: b.config(bg='#667eea'))

# Controls
control_frame = tk.Frame(root, bg='#1a1a2e')
control_frame.pack(pady=15)

stop_btn = tk.Button(control_frame, text="⏹ Stop", 
                    command=stop_music,
                    bg='#e74c3c', fg='white',
                    font=('Helvetica', 11),
                    width=8, relief='flat')
stop_btn.pack(side=tk.LEFT, padx=5)

web_btn = tk.Button(control_frame, text="🌐 Web UI", 
                   command=open_web,
                   bg='#2ecc71', fg='white',
                   font=('Helvetica', 11),
                   width=8, relief='flat')
web_btn.pack(side=tk.LEFT, padx=5)

# Volume
vol_frame = tk.Frame(root, bg='#1a1a2e')
vol_frame.pack(pady=15)

tk.Label(vol_frame, text="🔊 Volume", 
        bg='#1a1a2e', fg='white',
        font=('Helvetica', 10)).pack()

volume = tk.Scale(vol_frame, from_=0, to=100, 
                 orient=tk.HORIZONTAL,
                 bg='#1a1a2e', fg='white',
                 troughcolor='#667eea',
                 highlightthickness=0,
                 command=set_volume)
volume.set(80)
volume.pack()

# Status
status_label = tk.Label(root, text="Ready - Click a song to play",
                       bg='#1a1a2e', fg='#95a5a6',
                       font=('Helvetica', 10))
status_label.pack(pady=10)

# Footer
tk.Label(root, text="Playing on WILLEN",
        bg='#1a1a2e', fg='#7f8c8d',
        font=('Helvetica', 9)).pack(side=tk.BOTTOM, pady=10)

root.mainloop()

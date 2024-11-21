import yt_dlp
import tkinter as tk
from tkinter import filedialog

# Initialize Tkinter root window (it will not show)
root = tk.Tk()
root.withdraw()  # Hide the root window

# Ask the user for the playlist URL
playlist_url = input('Playlist URL: ')

# Ask the user to choose the format (mp3/mp4)
format_choice = input('Format (mp3/mp4): ').strip().lower()

# Initialize the quality variable and set the correct options
if format_choice == 'mp3':
    # If mp3, ask for audio quality
    quality = input('Audio Quality (128/256/320): ').strip().lower()
    if quality not in ['128', '256', '320']:
        print("Invalid quality choice. Defaulting to 320.")
        quality = '320'
    
    # Set the yt-dlp options for mp3 download
    ydl_opts = {
        'outtmpl': 'Music/%(title)s.%(ext)s',  # Save mp3 files
        'format': f'bestaudio[ext=m4a]/bestaudio[ext=webm]/bestaudio[ext=mp3]',
        'audio-quality': f'{quality}K',  # Specify audio quality
        'noplaylist': False,  # Download the full playlist
        'progress_hooks': [lambda d: print(f"Downloading {d['filename']}...")],  # Print progress
    }

elif format_choice == 'mp4':
    # If mp4, ask for video quality
    quality = input('Video Quality (480p/720p/1080p): ').strip().lower()
    if quality not in ['480p', '720p', '1080p']:
        print("Invalid quality choice. Defaulting to 480p.")
        quality = '480p'
    
    # Set the yt-dlp options for mp4 download
    ydl_opts = {
        'outtmpl': 'Videos/%(title)s.%(ext)s',  # Save videos
        'format': f'bestvideo[ext=mp4][height<={quality}]+bestaudio[ext=m4a]/bestvideo[ext=webm][height<={quality}]+bestaudio[ext=webm]',
        'merge-output-format': 'mp4',  # Merge audio and video into mp4 format
        'noplaylist': False,  # Download the full playlist
        'progress_hooks': [lambda d: print(f"Downloading {d['filename']}...")],  # Print progress
    }

else:
    print("Invalid format choice. Exiting...")
    exit()

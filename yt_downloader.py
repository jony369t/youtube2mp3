#!/usr/bin/env python3
"""
YouTube to MP3 Downloader
Download a list of YouTube videos as MP3 files.
"""

import os
import sys
import subprocess
import time

def check_dependencies():
    """Verify required packages and tools are installed"""
    try:
        import yt_dlp
    except ImportError:
        print("✖ Error: yt-dlp not installed in current environment.")
        print("Please install it using: pip install -r requirements.txt")
        sys.exit(1)
    
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✖ Error: FFmpeg not found or not in PATH")
        print("Please install FFmpeg and ensure it's accessible in your system's PATH.")
        print("See installation instructions at: https://ffmpeg.org/download.html")
        sys.exit(1)

def download_songs(url_list, output_dir='./downloads'):
    """Download YouTube videos as MP3 files"""
    os.makedirs(output_dir, exist_ok=True)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ignoreerrors': True,  # Skip errors on individual videos
        'progress_hooks': [progress_hook],
    }

    print(f"ℹ Starting download of {len(url_list)} songs...")
    start_time = time.time()
    
    import yt_dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.download(url_list)
    
    duration = time.time() - start_time
    print(f"\n✔ Processing completed in {duration:.1f} seconds!")
    print(f"🎵 Files saved to: {os.path.abspath(output_dir)}")
    return result

def progress_hook(d):
    """Display download progress"""
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', 'N/A')
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        # Truncate the filename to avoid flooding the console
        filename = os.path.basename(d.get('filename', 'Unknown'))
        if len(filename) > 30:
            filename = filename[:27] + '...'
        print(f"\r⏬ {filename}: {percent} at {speed} | ETA: {eta}", end='', flush=True)
    elif d['status'] == 'finished':
        filename = os.path.basename(d.get('filename', 'Unknown'))
        print(f"\n✔ Downloaded: {filename}")

if __name__ == '__main__':
    check_dependencies()
    
    # Always load URLs from file
    url_file = 'urls.txt'
    if not os.path.exists(url_file):
        print(f"✖ Error: Create '{url_file}' with YouTube URLs first!")
        print("Each URL should be on a separate line")
        print("Example: https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        sys.exit(1)
    
    with open(url_file, 'r') as f:
        urls = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    if not urls:
        print(f"ℹ No valid URLs found in {url_file}")
        sys.exit(0)
        
    print(f"ℹ Loaded {len(urls)} URLs from {url_file}")
    download_songs(urls)

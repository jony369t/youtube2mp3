# YouTube to MP3 Downloader

A Python script to download a list of YouTube videos as MP3 files.

 ![image](https://github.com/user-attachments/assets/d1f7c6e7-ffb2-4809-9a3b-80274d0a03d5)



## Features

- Batch download YouTube videos as MP3 files
- Simple text-based interface
- Progress tracking
- Automatic folder creation
- Error skipping for invalid URLs
- Fast conversion with FFmpeg

## Requirements

- Python 3.6+
- [FFmpeg](https://ffmpeg.org/)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jony369t/youtube2mp3.git
cd youtube-mp3-downloader
```
2.Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Usage
 Add YouTube URLs to urls.txt (one per line)
 Run the script:
```bash
python yt_downloader.py
```
5. Configuration
   *Edit urls.txt to change the list of videos
   *Modify the script to change output directory (default: downloads/)
   *Change audio quality by modifying 'preferredquality': '192' in the     script

## YouTube Playlist Downloader (Python)

Youtube_Downloader is a Python script that allows you to download entire YouTube playlists either in MP3 or MP4 format. The tool uses the powerful yt-dlp library, which provides enhanced functionality over the traditional youtube-dl, and is capable of handling a wide variety of media formats and quality settings.

### Features
- Download Playlists: Supports downloading entire YouTube playlists.
- Select Audio/Video Format: Choose to download in either MP3 (audio) or MP4 (video) format.
- Customizable Quality: Select the video/audio quality (e.g., 480p, 720p, best audio).
- Folder Selection: Allows you to select the destination folder where the downloaded files will be saved using a simple file dialog.
- Error Handling: Skips over any videos that fail to download, ensuring the rest of the playlist is still downloaded.

### Prerequisites
- Python 3.x
- yt-dlp: Install using pip install yt-dlp.
- Tkinter: Comes pre-installed with Python for GUI support.
- cookies.txt: Required for bypassing restrictions like age verification. Can be obtained from your browser.

### Usage
1. Clone or download the repository.
2. Run the main.py script.
3. Input the YouTube playlist URL when prompted.
4. Select the format (mp3 for audio or mp4 for video).
5. Choose the folder where the files will be saved.
6. The script will begin downloading the playlist. All files will be saved in the selected folder.

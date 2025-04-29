# ytdlp-gui-linux

A simple graphical YouTube downloader for Linux, built with PySide6 and [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Features

- Clean, modern GUI for downloading videos using yt-dlp
- Dark mode interface
- Download progress indicator (spinner)
- Status messages for download progress and completion

## Requirements

- Python 3.7+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- PySide6

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ytdlp-gui-linux.git
cd ytdlp-gui-linux
```

### 2. Set up a virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download yt-dlp (if not already installed)

```bash
pip install yt-dlp
```

Or, to use the standalone binary, download it from the [yt-dlp releases page](https://github.com/yt-dlp/yt-dlp/releases) and place it in your project directory.

### 5. Run the app

```bash
python gui.py
```

## Usage

1. Paste a YouTube (or other supported site) URL into the text box.
2. Click "Submit".
3. The app will show a spinner and "Downloading..." status.
4. When the download is complete, the status will change to "Download Complete!".

## Project Structure

```
.
├── gui.py            # Main application code
├── requirements.txt  # Python dependencies
├── spinner.gif       # Spinner animation (place your own if needed)
├── venv/             # Virtual environment (not tracked by git)
├── .gitignore
└── README.md
```

## Customization

- To change the look and feel, edit the dark mode stylesheet in `gui.py`.
- To change the spinner, replace `spinner.gif` with your preferred animation.

## License

MIT License

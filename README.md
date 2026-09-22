# Media Library App

A desktop GUI application built with Python and Tkinter to catalog and organize personal media collections across physical and digital formats.

## Overview

I built this application to have a simple, local-first way to keep track of my physical collection (CDs, DVDs) alongside digital releases (FLAC, MP3, streaming). Everything is stored locally in human-readable JSON without requiring any third-party service or heavy database setup.

## Features

- **Multi-Category Tracking**: Catalog Music, Movies, TV Shows, and Podcasts.
- **Physical & Digital Formats**: Tag items by format (CD, DVD, FLAC, MP3, MP4, Streaming).
- **CRUD Operations**:
  - Add new media items with type, format, title, artist/creator, and release year.
  - View all stored entries in an interactive listbox.
  - Load and update existing entries.
  - Remove individual items or clear the library.
- **Persistent Storage**: Data is automatically saved to and loaded from `app_info.json` with UTF-8 encoding.
- **Input Validation**: Verifies field inputs (e.g. numeric release year) to prevent corrupted entries.

## Project Structure

```text
media-library-app/
├── build_v1/
│   ├── gui_app.py      # Tkinter GUI interface and event handling
│   ├── media_item.py   # MediaItem class model and JSON serialization
│   └── app_info.json   # Local JSON data storage
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8+
- Tkinter (standard with Python on most systems)

On Linux, if Tkinter is not already installed:
```bash
# Fedora
sudo dnf install python3-tkinter

# Debian / Ubuntu
sudo apt install python3-tk
```

### Running the App

1. Clone the repository:
```bash
git clone https://github.com/Spoukywo/MediaLibraryApp.git
cd MediaLibraryApp
```

2. Launch the interface:
```bash
python3 build_v1/gui_app.py
```

### CLI Mode

The core `MediaItem` model can also be executed directly in the terminal for quick testing:
```bash
python3 build_v1/media_item.py
```

## Planned Improvements

- [ ] Search and filter entries by artist, year, or format
- [ ] Export and import library to CSV
- [ ] Cover art preview
- [ ] SQLite backend option for larger libraries

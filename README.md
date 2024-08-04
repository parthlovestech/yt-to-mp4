## How to Use It

### Overview

This repository contains a Python script that allows you to download YouTube videos to your local machine. The script uses the `yt-dlp` library, a powerful tool for downloading high-quality YouTube videos and audio.

### Prerequisites

1. **Python**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/).

2. **yt-dlp**: This script requires the `yt-dlp` library. You can install it using pip.

### Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/parthlovestech/yt-to-mp4.git
   cd yt-to-mp4
   ```

2. **Install Dependencies**:
   Install the `yt-dlp` library using pip:
   ```sh
   pip install yt-dlp
   ```

### Usage

1. **Run the Script**:
   Navigate to the directory containing the script and run it using Python:
   ```sh
   python let-me-cook.py
   ```

2. **Provide Input**:
   When prompted, enter the URL of the YouTube video you want to download.

   - **Example URL**: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`

   Next, enter the directory path where you want to save the video. Press Enter to use the current directory.

3. **Download Process**:
   The script will download the video to the specified directory and provide information about the download, including the title, views, and duration of the video.

### Example

```sh
$ python let-me-cook.py
Enter the YouTube video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Enter the download path (or press Enter to use the current directory): /path/to/save/directory
```

### Notes

- Ensure that the specified download path exists and is writable.
- If you encounter any issues, check the permissions of the directory or try running the script with elevated privileges.

For more detailed information about `yt-dlp` and its options, visit the [yt-dlp GitHub page](https://github.com/yt-dlp/yt-dlp).

---


import yt_dlp
import os

def download_video(url, path='~/videos'):
    if not os.path.exists(path):
        print(f"The specified path {path} does not exist.")
        return
    
    try:
        ydl_opts = {
            'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
            'format': 'bestvideo+bestaudio/best',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            print(f"Title: {info_dict.get('title')}")
            print(f"Views: {info_dict.get('view_count')}")
            print(f"Duration: {info_dict.get('duration')} seconds")
            print(f"Downloaded to: {path}/{info_dict.get('title')}.{info_dict.get('ext')}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_path = input("Enter the download path (or press Enter to use the current directory): ")
    if not download_path:
        download_path = '.'
    download_video(video_url, download_path)

from pytube import YouTube
import os

def download_youtube_video():
    # Get the video URL from the user
    video_url = input("Enter the YouTube video URL: ")
    
    # Specify the download directory
    download_dir = input("Enter the download directory or leave blank to use the current directory: ")
    if not download_dir:
        download_dir = os.getcwd()
    
    try:
        # Create a YouTube object
        yt = YouTube(video_url)
        
        # Get the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()
        
        # Display some video details
        print(f"Title: {yt.title}")
        print(f"Views: {yt.views}")
        print(f"Duration: {yt.length} seconds")
        
        # Start downloading
        print("\nDownloading...")
        video_stream.download(output_path=download_dir)
        print(f"Video downloaded successfully and saved to: {download_dir}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_youtube_video()
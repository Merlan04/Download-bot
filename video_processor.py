import yt_dlp

def download_video(url):
    # Set up yt_dlp options
    ydl_options = {
        'retry_count': 5,
        'geo_bypass_country': 'US',
        'sleep_interval': 1,
        'api_hostname': ['api.tiktok.com', 'youtube.googleapis.com'],
        'player_client': ['desktop', 'mobile'],
        'outtmpl': '%(title)s.%(ext)s',  # Customize output template
    }

    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.download([url])

# Example usage
# download_video('your_video_url')
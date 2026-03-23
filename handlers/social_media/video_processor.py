import yt_dlp

class VideoProcessor:
    def __init__(self, geo_region=None):
        # Initialize with geo-region options for yt-dlp
        self.geo_region = geo_region

    def download_video(self, url):
        ydl_opts = {
            'geo_bypass': True,
            'geo''_location': self.geo_region,  # Set the geo-region based on initialization
            'format': 'best',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except yt_dlp.utils.ExtractorError as e:
            print(f'Error downloading video from TikTok: {e}')  # Improved error handling for TikTok\n        except Exception as e:
            print(f'An unexpected error occurred: {e}')

import os
from googleapiclient.discovery import build
from pytube import YouTube
from urllib.parse import urlparse, parse_qs

from models.video import Video


class YouTubeDownloader:

    def __init__(self, key: str, url: str):
        self.key = key
        self.url = url


    def fetch_details(self):
        youtube = build('youtube', 'v3', developerKey=self.key)
        
        # The video id is included in the url of each YouTube video.
        # We parse the url in order to obtain the query parameters.
        params = parse_qs(urlparse(self.url).query)

        # The 'v' parameter is the one that specifies the video id.
        video_id = params['v']
        response = youtube.videos().list(part=['snippet', 'statistics'], id=video_id).execute()

        # Instead of the complete response,
        # we return a Video object with the metadata that we're interested in.

        title = response['items'][0]['snippet']['title']
        publication_date = response['items'][0]['snippet']['publishedAt']
        views = response['items'][0]['statistics']['viewCount']

        return Video(video_id, self.url, title, publication_date, views)
    

    def download_video(self, path, name):
        yt = YouTube(self.url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4')
        try:
            stream.order_by('resolution').desc().first().download(output_path=path, filename=name)
        except Exception as e:
            print('Error while downloading: ' + e)
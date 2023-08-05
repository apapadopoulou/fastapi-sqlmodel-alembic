import os
from googleapiclient.discovery import build
from urllib.parse import urlparse, parse_qs

# The API key is set as an environment parameter.
api_key = os.environ.get('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


def fetch_video(url: str):
    video_id = get_video_id(url)
    response = youtube.videos().list(part=['contentDetails', 'snippet', 'statistics'], id=video_id).execute()
    return response

def get_video_id(url: str):

    # The video id is included in the url of each YouTube video.
    # We parse the url in order to obtain the query parameters.
    params = parse_qs(urlparse(url).query)

    # The 'v' parameter is the one that specifies the video id.
    return params['v']
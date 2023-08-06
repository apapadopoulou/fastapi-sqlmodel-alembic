from fastapi import Depends, FastAPI
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
import os

from app.db import get_session, init_db

from models.youtube_downloader import YouTubeDownloader
from models.audio_converter import AudioConverter

app = FastAPI()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/video")
async def fetch_video_detals(url: str = None):
    if url is None:
        return "Sorry, you have to provide a url parameter! :("

    # The API key is already stored as an environment variable.
    api_key = os.environ.get('YOUTUBE_API_KEY')

    # Initialize downloader and fetch song details
    # by using a video object.
    downloader = YouTubeDownloader(api_key, url)
    video = downloader.fetch_details()

    # Download video.
    downloader.download_video('./files/', f'{video.title}.mp4')

    # Convert downloaded video to audio.
    converter = AudioConverter()
    converter.convert_to_audio(f'./files/{video.title}.mp4', f'./files/{video.title}.mp3')

    # Return video details.
    return video.get_video_details()
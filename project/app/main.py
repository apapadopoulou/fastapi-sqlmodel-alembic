from fastapi import Depends, FastAPI
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.db import get_session, init_db
from app.models import Song, SongCreate
from downloader.fetch_song_details import fetch_video

app = FastAPI()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/video")
async def fetch_video_detals(url: str = None):
    if url is None:
        return "what?"
    video = fetch_video(url)
    return video
import asyncio
from shazamio import Shazam, Serialize

from models.song import Song

class SongIdentifier:

    def __init__(self, audio_file):
        self.audio_file = audio_file

    async def get_song(self):
        shazam = Shazam()
        output = await shazam.recognize_song(self.audio_file)

        try:
            
            # We serialize the data in order to handle them more easily.
            serialized = Serialize.full_track(output)

            # We only keep the metadata we're interested in.
            apple_music_url = serialized.track.apple_music_url
            spotify_url = serialized.track.spotify_url

        except Exception as e:
            print('Error while recognizing audio: ' + e)

        return Song(apple_music_url, spotify_url)

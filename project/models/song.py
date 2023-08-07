
class Song:

    def __init__(self, apple_music_url, spotify_url):
        self.apple_music_url = apple_music_url
        self.spotify_url = spotify_url

    def get_song_details(self):
        return f'{self.apple_music_url}, {self.spotify_url}'
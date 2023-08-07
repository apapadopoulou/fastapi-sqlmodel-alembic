
class Song:

    def __init__(self, apple_music_url, spotify_url):
        self.apple_music_url = apple_music_url
        self.spotify_url = spotify_url

    # Return a string with song attributes.
    def get_song_details(self):
        return f'{self.apple_music_url}, {self.spotify_url}'
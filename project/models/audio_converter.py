from pydub import AudioSegment

class AudioConverter:

    # Converts the provided video file into audio.
    def convert_to_audio(self, vid_path, aud_path):
        try:
            audio = AudioSegment.from_file(vid_path)
            audio.export(aud_path, format='mp3')

        except Exception as e:
            print('Error while converting to audio:', e)
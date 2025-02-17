from pydub import AudioSegment
from pydub.playback import play

def play_audio(filename="output.wav"):
    audio = AudioSegment.from_wav(filename)
    play(audio)

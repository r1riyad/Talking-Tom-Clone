import pyaudio
import wave

def record_audio(filename="input.wav", duration=5, rate=44100, channels=1):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=channels, rate=rate, input=True, frames_per_buffer=1024)
    
    print("Recording... 🎤")
    frames = [stream.read(1024) for _ in range(0, int(rate / 1024 * duration))]
    print("Recording finished! ✅")

    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

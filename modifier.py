import os

def modify_audio(input_file="input.wav", output_file="output.wav", pitch=1.5):
    command = f'ffmpeg -y -i {input_file} -filter:a "asetrate=44100*{pitch},atempo=1/{pitch}" {output_file}'
    os.system(command)
    print("Voice modified successfully! 🎙️")

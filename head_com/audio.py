import numpy as np
import sounddevice as sd
import soundfile as sf
from gtts import gTTS
import os

def play_sound(file_path, output_device_index=None):
    data, fs = sf.read(file_path, dtype='float64')
    sd.play(data, fs, device=output_device_index)
    sd.wait()

def play_audio(text, index, lang):
    tts = gTTS(text=text, lang=lang)
    
    audio_file = "output.mp3"
    tts.save(audio_file)

    play_sound(audio_file, index)

    play_sound(audio_file)

    os.remove(audio_file)
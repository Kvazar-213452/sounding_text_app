# sounding_text_app

import numpy as np
import sounddevice as sd
import soundfile as sf
from gtts import gTTS
import os

def play_sound(file_path, output_device_index=None):
    data, fs = sf.read(file_path, dtype='float64')
    sd.play(data, fs, device=output_device_index)
    sd.wait()

while True:
    text = input("Введіть текст для озвучення (або 'exit' для виходу): ")

    if text.lower() == 'exit':
        print("Вихід з програми.")
        break

    tts = gTTS(text=text, lang='uk')
    
    audio_file = "output.mp3"
    tts.save(audio_file)

    print("Відтворення через віртуальний кабель...")
    play_sound(audio_file, 6)
    
    print("Відтворення через стандартні динаміки...")
    play_sound(audio_file)
    
    print("Озвучений текст:")

    os.remove(audio_file)


import os

import openai

openai.api_key = "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"
# openai.api_base = "https://api.openai.com/v1"
openai.api_base = "https://api.laibutech.com/v1" 

def read(filename):
    print("转换中")
    audio_file = open(filename, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print(transcript['text'])
    return transcript['text']



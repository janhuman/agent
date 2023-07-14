import time
import streamlit as st
from scipy.io.wavfile import write
import sounddevice as sd
from lbai_agent import transfer
from redis_utils import pub_sub

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

channal = "1"

def record_audio():
    st.write("开始录音...")
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    st.write("录音结束")
    write('output.mp3', fs, myrecording)  # Save as MP3 file
    time.sleep(1)
    user_speak = transfer.read('output.mp3')
    time.sleep(1)
    pub_sub.publish_message(channal, user_speak)
    st.write(user_speak)

if st.button('录音/保存'):
    record_audio()


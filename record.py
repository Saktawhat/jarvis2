"""
    Predict WakewordIN
"""

import numpy as np
import torch # onnxruntime stupid as shit cant find CUDA path so torch is needed LOL
import sounddevice as sd
import openwakeword
from openwakeword.model import Model

WAKE_THRESHOLD = 0.30
RATE=16000
CHUNKSIZE = 1024

#Download model (Leave empty for all models)
model = Model(wakeword_model_paths=["/run/media/whatdafaq/Cachy2/projects/jarvis2/hey_jarvis_v0.1.onnx"])

def callback(indata, frames, time, status):
    if status:
        print(status)

    audio = np.frombuffer(indata, dtype='int16')
    prediction = model.predict(audio)
    for name, score in prediction.items():
        if score >= WAKE_THRESHOLD:
            print(f"wakeword detected: {name} ({score:.2f})")


if __name__ == "__main__":
    with sd.InputStream(channels=1, callback=callback, samplerate=RATE, dtype='int16', blocksize=CHUNKSIZE):
        print("streaming started..")
        while True:
            sd.sleep(1000)

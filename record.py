"""
    Predict wakeword using ONNX models
"""
import numpy as np
import torch # onnxruntime stupid as shit cant find CUDA path so torch is needed LOL
import sounddevice as sd
import openwakeword
from openwakeword.model import Model

WAKE_THRESHOLD = 0.30
RATE=16000
CHUNKSIZE = 1280
WAKEWORD = "./wakeword.onnx"

#Download model (Leave empty for all models)
model = Model(wakeword_model_paths=[WAKEWORD])

def callback(indata, frames, time, status):
    if status:
        print(status)
        return

    audio_data = indata[:, 0].copy()
    prediction = model.predict(audio_data)

    print("Detecting...", prediction)
    for name, score in prediction.items():
        if score >= WAKE_THRESHOLD:
            print(f"wakeword detected: {name} ({score:.2f})")


def inpstream():
    with sd.InputStream(channels=1, callback=callback, samplerate=RATE, dtype='int16', blocksize=CHUNKSIZE):
        print("streaming started..")
        while True:
            sd.sleep(1000)

if __name__ == "__main__":
    inpstream()

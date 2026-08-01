import sounddevice as sd
import numpy as np
import openwakeword
from openwakeword.model import Model

# Load model
openwakeword.utils.download_models() 

#Download model (Leave empty for all models)
model = Model(
    wakeword_models=[],
)


def callback(indata, outdata, frames, time, status):
    if status:
        print(status)

def wakeword_detection():
    with sd.InputStream(channels=1,samplerate=16000,dtype='int16',blocksize=1024, callback=callback): #capture mic
        print("listening.......")

        while True:
            frame = wakeword_detection()
            prediction = model.predict(frame)
    






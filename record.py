import numpy as np
import edgetest as ei
import sounddevice as sd

# CONF
WAKE_THRESHOLD = 0.30
RATE=16000
CHUNKSIZE = 1280
WAKEWORD = "./wakeword.onnx"

ei.API_KEY = "ei_ce824ae2b29c2058294c8b38cee3d3d1c6c7d8592b2020ad"

def callback(indata, frames, time, status):
    if status:
        print(status)
        return

    audio_data = indata[:, 0].copy()



def inpstream():
    with sd.InputStream(channels=1, callback=callback, samplerate=RATE, dtype='int16', blocksize=CHUNKSIZE):
        print("streaming started..")
        while True:
            sd.sleep(1000)

if __name__ == "__main__":
    inpstream()

import pyaudio
import numpy as np
import sounddevice as sd
import openwakeword
from openwakeword.model import Model

WAKE_THRESHOLD = 0.30
duration = 10
RATE=16000
CHUNKSIZE = 1024

#Download model (Leave empty for all models)
model = Model(wakeword_model_paths=["/run/media/whatdafaq/Cachy2/projects/jarvis2/hey_jarvis_v0.1.onnx"])

def callback(indata, frames, time, status):
    if status:
        print(status)


# Stream opened
with sd.InputStream(channels=1, callback=callback,samplerate=RATE,dtype='int16',blocksize=CHUNKSIZE):
    print("streaming...")
    sd.sleep(int(duration * 1000))

if __name__ == "__main__":
    while True:
        audio = np.frombuffer(sd.Stream.read(1280), dtype='int16')
        prediction = model.predict(audio)
        print(prediction)
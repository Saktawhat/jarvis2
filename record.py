import sounddevice as sd
import numpy as np
import openwakeword
from openwakeword.model import Model

WAKE_THRESHOLD = 0.30
duration = 10

#Download model (Leave empty for all models)
model = Model(wakeword_model_paths=["/run/media/whatdafaq/Cachy2/projects/jarvis2/hey_jarvis_v0.1.onnx"])

# get the indata from RawStream (according to docs) 
def callback(indata, frames, time, status):
    if status:
        print(status)

    # convert from raw python buffer into np array
    frame = np.frombuffer(indata, dtype=np.int16)
    frame = frame.reshape(-1) #got the frame rn

    # Todo: Pass the frame into the processing pipeline (is there even one? <- there IS one, but not for inpStream)
    
    


# Raw results in python buffer
with sd.RawInputStream(channels=1, dtype='int16', callback=callback, samplerate=16000, blocksize=1280):
    print("listening...")
    sd.sleep(int(duration * 1000))

            
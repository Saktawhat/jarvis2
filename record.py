import sounddevice as sd
import numpy as np
import openwakeword
from openwakeword.model import Model

vad_threshold = 0.30

#Download model (Leave empty for all models)
model = Model(wakeword_models=["hey_jarvis"]) # << CHANGE THIS TO ACTUAL USABLE MODEL (hey jarvis)

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)

with sd.InputStream(channels=1,samplerate=44100,dtype='int16',blocksize=1280, callback=callback): #capture mic
    print("listening.......")

    while True:
        audio, overflowed = Stream.read(1280)
        frame = audio.reshape(-1).astype(np.int16)

        prediction = model.predict(frame) #predict the wakeword
        if prediction.get("hey_jarvis", 0) > vad_threshold:
            print("detected")
            
            # continue to main processing



if __name__ == "__main__":
    pass



    

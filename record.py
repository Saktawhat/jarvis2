import sounddevice as sd
import numpy as np
import openwakeword
from openwakeword.model import Model
from process import DecodeAudio

vad_threshold = 0.30
duration = 10

#Download model (Leave empty for all models)
model = Model(wakeword_models=["/run/media/whatdafaq/Cachy2/projects/jarvis2/hey_jarvis_v0.1.tflite"]) # << CHANGE THIS TO ACTUAL USABLE MODEL (hey jarvis)
enable_speex_noise_suppression=True

# get the indata from RawStream (according to docs)
def callback(indata,frames, time, status):
    if status:
        print(status)
        frame = indata.reshape(-1).astype(np.int16)
        prediction = model.predict(frame) #predict the wakeword
        confidence = prediction.get("hey_jarvis", 0.0)

        # somehow needs to get conf value here
        if confidence > vad_threshold:
            print("detected")
                
            rec = sd.rec(int(8 * 16000), samplerate=16000, channels=1, dtype='int16')
            sd.wait()
            print("recording complete")
            # either call or save

with sd.RawStream(channels=1, dtype='int16', callback=callback):
    sd.sleep(int(duration * 1000))

            
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wavfile


def record_audio(duration=15, fs=16000):
    print("Jarvis is listening...")
    # อัดเสียงและเก็บใน NumPy array (DataType เป็น float32 ตามที่ AI ส่วนใหญ่ต้องการ)
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()  # รอจนกว่าจะอัดเสร็จ
    print("Recording finished.")
    
    # Save the recording to a temporary file
    filename = "temp_audio.wav"
    wavfile.write(filename, fs, recording)
    return filename

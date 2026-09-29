# TASK: TEST THE MODELS ACCURACY WITH MY VOICE AND WITH SAMPLES
# DUE: SUNDAY (BETER DO IT NGA)

import sounddevice as sd
import numpy as np
from openwakeword.utils import AudioFeatures
from openwakeword.model import Model

model = Model=["/run/media/whatdafaq/Cachy2/projects/jarvis2/hey_jarvis_v0.1.tflite"]
model.predict_clip("/run/media/whatdafaq/Cachy2/projects/jarvis2/asset/ElevenLabs_2026-08-21T17_37_24_Toto - Warm Thai Storyteller_pvc_sp100_s50_sb75_se0_b_m2.mp3")




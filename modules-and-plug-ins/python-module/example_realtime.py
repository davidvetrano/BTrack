import sounddevice as sd
import numpy as np
import btrack

def process_frame(indata, frames, time, status):
    indata_mono = np.mean(indata, axis=1)
    if btrack.processAudioFrame(indata_mono):
        print("beat")

with sd.InputStream(device=0, blocksize=512, samplerate=44100, channels=2, callback=process_frame):
    sd.sleep(10000)

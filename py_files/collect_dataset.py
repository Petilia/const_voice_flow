import pyaudio
import wave
import os
import soundfile as sf
from pyaudio_tools import get_device_index
    
base_folder = "asr_dataset/"
speaker_folder = "petryashin/"
exp = "simple_comands.wav"
filename = os.path.join(base_folder, speaker_folder, exp) 

if not os.path.isdir(base_folder):
    os.mkdir(base_folder)

if not os.path.isdir(os.path.join(base_folder, speaker_folder)):
    os.mkdir(os.path.join(base_folder, speaker_folder))


chunk=1024
sample_format=pyaudio.paInt16
channels=1
rate=16000
input_device_index = get_device_index()

p = pyaudio.PyAudio() # Создать интерфейс для PortAudio

stream = p.open(format=sample_format,
        channels=channels,
        rate=rate,
        frames_per_buffer=chunk,
        input_device_index=input_device_index, # индекс устройства с которого будет идти запись звука 
        input=True)

frames = [] 

try:
    while True:
            data = stream.read(chunk, exception_on_overflow = False)
            frames.append(data)

except:
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()
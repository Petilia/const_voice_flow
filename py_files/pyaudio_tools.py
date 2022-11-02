import pyaudio
import wave
import os
import soundfile as sf

def listen_n_seconds(input_device_index, filename="heard_file.wav", base_folder="/home/appuser/py_files/",
                        chunk=1024, sample_format=pyaudio.paInt16, channels=1, 
                            rate=16000, seconds=3, convert_to_ogg=True):

    filename = os.path.join(base_folder, filename)

    p = pyaudio.PyAudio() # Создать интерфейс для PortAudio
    
    stream = p.open(format=sample_format,
            channels=channels,
            rate=rate,
            frames_per_buffer=chunk,
            input_device_index=input_device_index, # индекс устройства с которого будет идти запись звука 
            input=True)

    frames = [] 

    for i in range(0, int(rate / chunk * seconds)):
        data = stream.read(chunk, exception_on_overflow = False)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()

    #convert to ogg
    if convert_to_ogg:
        data, samplerate = sf.read(filename)
        ogg_name = filename[0:-4] + ".ogg"
        sf.write(ogg_name, data, samplerate)


def play_audio(filename, output_device_index, base_folder="/home/appuser/py_files/", chunk=1024, 
                        device_channels=1, device_rate=48000):

    filename = os.path.join(base_folder, filename)
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()

    stream = p.open(
        format = p.get_format_from_width(wf.getsampwidth()),
        channels = device_channels,
        rate = device_rate,
        output_device_index=output_device_index,
        output = True
        )
  
    data = wf.readframes(chunk)
    while data != b'':
        stream.write(data)
        data = wf.readframes(chunk)

    stream.close()
    p.terminate()


def get_device_index(device_name="Plantronics"):

    p = pyaudio.PyAudio()

    for i in range(p.get_device_count()):
        if device_name in p.get_device_info_by_index(i)['name']:
            index_device = i

    return index_device


def convert_2_48kHz(input_file, base_folder="/home/appuser/py_files/", convert_2_48k_file="temp_audio_file_48k.wav"):

    input_file = os.path.join(base_folder, input_file)
    convert_2_48k_file = os.path.join(base_folder, convert_2_48k_file)

    if os.path.isfile(convert_2_48k_file):
        os.remove(convert_2_48k_file)

    os.system(f"ffmpeg -i {input_file} -ar 48000 {convert_2_48k_file}")
    os.remove(input_file)



# class AudioFile:
#     chunk = 1024

#     def __init__(self, file, device_name="Plantronics", device_rate=48000, device_channels=1):
#         """ Init audio stream """ 
#         self.wf = wave.open(file, 'rb')
#         self.p = pyaudio.PyAudio()

#         # print(self.p.get_format_from_width(self.wf.getsampwidth()))
#         # print(self.wf.getframerate())
        
#         for i in range(self.p.get_device_count()):
#             if device_name in self.p.get_device_info_by_index(i)['name']:
#                 index_device = i

#         self.stream = self.p.open(
#             # format = pyaudio.paInt16,
#             format = self.p.get_format_from_width(self.wf.getsampwidth()),
#             channels = device_channels,
#             rate = device_rate,
#             output_device_index=index_device,
#             output = True
#         )

#     def play(self):
#         """ Play entire file """
#         data = self.wf.readframes(self.chunk)
#         while data != b'':
#             self.stream.write(data)
#             data = self.wf.readframes(self.chunk)

#     def close(self):
#         """ Graceful shutdown """ 
#         self.stream.close()
#         self.p.terminate()
import soundfile as sf
import time
import sys
import pyaudio
print(sys.version)

from speeckit_tools import asr_from_yandex_speeckit, listen_n_seconds


if __name__ == "__main__":

    p = pyaudio.PyAudio()

    for i in range(p.get_device_count()):
        if "Plantronics" in p.get_device_info_by_index(i)['name']:
            index_device = i
            # print(i, p.get_device_info_by_index(i))
            break
    
    FOLDER_ID = "b1gami13b761380nb5hb" # Идентификатор каталога
    API_KEY = "AQVN3XofRyHEW5PJOhBYCiObnGaZNYM8IvAQskdp" # API-ключ

    ogg_name = "ogg_file.ogg"
    wav_name = "wav_file.wav"

    while True:
        ###listen micro
        listen_n_seconds(wav_name, input_device_index=index_device)
        data, samplerate = sf.read(wav_name)
        sf.write(ogg_name, data, samplerate)
        asr_result = asr_from_yandex_speeckit(ogg_name, FOLDER_ID, API_KEY)
        print(asr_result)
        
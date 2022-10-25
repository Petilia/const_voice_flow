import soundfile as sf
import time
import sys
print(sys.version)

from speeckit_tools import asr_from_yandex_speeckit, listen_n_seconds


if __name__ == "__main__":
    
    FOLDER_ID = "b1gami13b761380nb5hb" # Идентификатор каталога
    API_KEY = "AQVN3XofRyHEW5PJOhBYCiObnGaZNYM8IvAQskdp" # API-ключ

    ogg_name = "ogg_file.ogg"
    wav_name = "wav_file.wav"

    const_ogg_name = "ogg_file1.ogg"

    while True:
        ###listen micro
        listen_n_seconds(wav_name)
        data, samplerate = sf.read(wav_name)
        sf.write(ogg_name, data, samplerate)
        asr_result = asr_from_yandex_speeckit(ogg_name, FOLDER_ID, API_KEY)
        # asr_result = asr_from_yandex_speeckit(const_ogg_name, FOLDER_ID, API_KEY)
        print("sdsds")
        
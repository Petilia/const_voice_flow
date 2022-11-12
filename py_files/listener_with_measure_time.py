import time
from speeckit_tools import asr_from_yandex_speeckit
from pyaudio_tools import listen_n_seconds, play_audio, get_device_index
import numpy as np

# Определяем, под каким индексом наш микрофон
index_device = get_device_index()


FOLDER_ID = "b1gami13b761380nb5hb" # Идентификатор каталога
API_KEY = "AQVN3XofRyHEW5PJOhBYCiObnGaZNYM8IvAQskdp" # API-ключ

ogg_name = "ogg_file.ogg"
wav_name = "wav_file.wav"

agent_url = "http://0.0.0.0:4242"

times = []

if __name__ == "__main__":

    try:
        while True:
            ###listen micro
            listen_n_seconds(index_device, seconds=1)
            t1 = time.time()
            asr_result = asr_from_yandex_speeckit(FOLDER_ID, API_KEY)
            delta_t = time.time() - t1
            times.append(delta_t)
            print(f"asr_result = {asr_result}, delta_t = {delta_t}")

    finally:
        times = np.array(times)
        print(times, times.shape)
        print(f"delta_t = {np.mean(times)} +- {np.std(times)}")


        # request to dream agent
        # cur_request = {"user_id":"xyz","payload":asr_result}
        # r = requests.post(url=agent_url, json=cur_request)
        # print('Request - ', cur_request['payload'], '\n', 'Response - ', r.json()['response'])
        
       
        
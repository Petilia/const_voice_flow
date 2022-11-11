import numpy as np
from pyaudio_tools import listen_n_seconds, get_device_index
from classifier_tools import get_logreg, get_data, get_statistics
import time

# Определяем, под каким индексом наш микрофон
index_device = get_device_index()


FOLDER_ID = "b1gami13b761380nb5hb" # Идентификатор каталога
API_KEY = "AQVN3XofRyHEW5PJOhBYCiObnGaZNYM8IvAQskdp" # API-ключ

ogg_name = "ogg_file.ogg"
wav_name = "wav_file.wav"

classifier_path = "/home/appuser/py_files/classifiers/dummy_logreg.pkl"
model = get_logreg(classifier_path)


times = []

if __name__ == "__main__":

    try:
        while True:
            ###listen micro
            listen_n_seconds(index_device)
            start_time = time.time()
            data = get_data(["/home/appuser/py_files/heard_file.wav"])
            features = get_statistics(data)
            pred = model.predict(features)
            delta_t = time.time() - start_time
            times.append(delta_t)
            print(f"pred_class = {pred}, delta_t = {delta_t}")
    finally:
        times = np.array(times)
        print(f"mean = {np.mean(times)}  std = {np.std(times)}")
        
        

      
        
       
        
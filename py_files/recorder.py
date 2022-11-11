import os
from pyaudio_tools import listen_n_seconds, get_device_index
from speeckit_tools import asr_from_yandex_speeckit
import pickle

FOLDER_ID = "b1gami13b761380nb5hb" # Идентификатор каталога
API_KEY = "AQVN3XofRyHEW5PJOhBYCiObnGaZNYM8IvAQskdp" # API-ключ

# Определяем, под каким индексом наш микрофон
index_device = get_device_index()

# exp = "noise"
# exp = "road_voice"
exp = "temp"
folder = "/home/appuser/py_files/records"

base_folder = os.path.join(folder, exp)
print(base_folder)

if not os.path.isdir(folder):
    os.mkdir(folder)
    print("mkdir folder")

if not os.path.isdir(base_folder):
    os.mkdir(base_folder)
    print("mkdir base_folder")

save_asr_result = True
if save_asr_result:
    pickle_path = os.path.join(base_folder, 'asr_results.pickle')
    asr_results = {}

if __name__ == "__main__":
    n = 0

    try:
        while True:
            ###listen micro
            print(f'Number {n} begins')
            filename = f"audio_{n}.wav"

            if not save_asr_result:
                listen_n_seconds(index_device, base_folder=base_folder, filename=filename, convert_to_ogg=False)
            elif save_asr_result:
                ogg_name = listen_n_seconds(index_device, base_folder=base_folder, filename=filename, 
                                                            convert_to_ogg=True, return_ogg_name=True)

                asr_results[filename] = asr_from_yandex_speeckit(FOLDER_ID, API_KEY, 
                                                                    base_folder=base_folder, audiofile_name=ogg_name)
                print(asr_results[filename])

            n += 1

    finally:
        with open(pickle_path, 'wb') as handle:
            pickle.dump(asr_results, handle, protocol=pickle.HIGHEST_PROTOCOL)




      

   
        
       
        
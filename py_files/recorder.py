import os
from pyaudio_tools import listen_n_seconds, get_device_index

# Определяем, под каким индексом наш микрофон
index_device = get_device_index()

exp = "noise"
folder = "/home/appuser/py_files/records"

base_folder = os.path.join(folder, exp)
print(base_folder)

if not os.path.isdir(folder):
    os.mkdir(folder)
    print("mkdir folder")

if not os.path.isdir(base_folder):
    os.mkdir(base_folder)
    print("mkdir base_folder")


if __name__ == "__main__":

    n = 0
    while True:
        ###listen micro
        print(f'Number {n} begins')
        listen_n_seconds(index_device, base_folder=base_folder, filename=f"audio_{n}.wav", convert_to_ogg=False)
        n += 1
      

   
        
       
        
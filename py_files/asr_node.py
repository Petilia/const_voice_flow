import roslibpy
import time

#asr tools
from speeckit_tools import asr_from_yandex_speeckit
from pyaudio_tools import listen_n_seconds, play_audio, get_device_index
import requests

index_device = get_device_index()

client = roslibpy.Ros(host='localhost', port=9090)
client.run()

FOLDER_ID = "b1gami13b761380nb5hb" # Идентификатор каталога
API_KEY = "AQVN3XofRyHEW5PJOhBYCiObnGaZNYM8IvAQskdp" # API-ключ

talker = roslibpy.Topic(client, '/asr_message', 'std_msgs/String')

while client.is_connected:
    listen_n_seconds(index_device)
    asr_result = asr_from_yandex_speeckit(FOLDER_ID, API_KEY)
    talker.publish(roslibpy.Message({'data': asr_result}))
    print(f'Sending message {asr_result}')

talker.unadvertise()

client.terminate()
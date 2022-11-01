import soundfile as sf


from speeckit_tools import asr_from_yandex_speeckit, tts_from_yandex_speechkit
from pyaudio_tools import listen_n_seconds, play_audio, get_device_index, convert_2_48kHz

# Определяем, под каким индексом наш микрофон
index_device = get_device_index()

FOLDER_ID = "b1gami13b761380nb5hb" # Идентификатор каталога
API_KEY = "AQVN3XofRyHEW5PJOhBYCiObnGaZNYM8IvAQskdp" # API-ключ

ogg_name = "ogg_file.ogg"
wav_name = "wav_file.wav"

agent_url = "http://0.0.0.0:4242"

text = "Спасибо отлично скоро я уничтожу всех человеков"

if __name__ == "__main__":

    while True:
        ###listen micro
        listen_n_seconds(index_device)
        asr_result = asr_from_yandex_speeckit(FOLDER_ID, API_KEY)
        print(asr_result)
        # text = "Я услышал " + asr_result

        ##tts + convert to our sample_rate + play
        tts_from_yandex_speechkit(text, FOLDER_ID, API_KEY)
        convert_2_48kHz("tts_result.wav")
        play_audio("temp_audio_file_48k.wav", index_device)

        # request to dream agent
        # cur_request = {"user_id":"xyz","payload":asr_result}
        # r = requests.post(url=agent_url, json=cur_request)
        # print('Request - ', cur_request['payload'], '\n', 'Response - ', r.json()['response'])
        
       
        
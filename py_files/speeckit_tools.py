import urllib
import urllib.request
import json
import requests
import os
import soundfile as sf

def asr_from_yandex_speeckit(FOLDER_ID, API_KEY, 
                                language="ru-RU", base_folder="/home/appuser/py_files/",
                                audiofile_name="heard_file.ogg" ):
    
    audiofile_name = os.path.join(base_folder, audiofile_name)

    with open(audiofile_name, "rb") as f:
        data = f.read()

    params = "&".join([
        "topic=general",
        "folderId=%s" % FOLDER_ID,
        "lang=%s" % language
    ])

    url = urllib.request.Request("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?%s" % params, data=data)
    url.add_header("Authorization", "Api-Key %s" % API_KEY) # если API-ключ
    # url.add_header("Authorization", "Bearer %s" % IAM_TOKEN) # если IAM токен

    responseData = urllib.request.urlopen(url).read().decode('UTF-8')
    decodedData = json.loads(responseData)

    if decodedData.get("error_code") is None:
        asr_result = decodedData.get("result")
    else:
        asr_result = 'Nothing recognized'
    
    return asr_result


def synthesize(folder_id, api_key, text):
    url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
    headers = {
        'Authorization': 'Api-Key ' + api_key,
    }

    data = {
        'text': text,
        'lang': 'ru-RU',
        'voice': 'filipp',
        'folderId': folder_id
    }

    with requests.post(url, headers=headers, data=data, stream=True) as resp:
        # print("request posted")
        if resp.status_code != 200:
            raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))

        
        for chunk in resp.iter_content(chunk_size=None):
            # print("chunk returned")
            yield chunk
            

def tts_from_yandex_speechkit(text, FOLDER_ID, API_KEY, tts_ogg_name="tts_result.ogg", base_folder="/home/appuser/py_files/"):

    tts_ogg_name = os.path.join(base_folder, tts_ogg_name)
    tts_wav_name = tts_ogg_name[0:-4] + ".wav"

    with open(tts_ogg_name, "wb") as f:
        for audio_content in synthesize(FOLDER_ID, API_KEY, text):
            f.write(audio_content)

    os.system(f"ffmpeg -i {tts_ogg_name} -ar 48000 {tts_wav_name}")

    # data, samplerate = sf.read(tts_ogg_name)
    # sf.write(tts_wav_name, data, samplerate)

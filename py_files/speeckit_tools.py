import urllib
import json

import pyaudio
import wave

def asr_from_yandex_speeckit(audiofile_name, FOLDER_ID, API_KEY, language="ru-RU"):
    
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


def listen_n_seconds(filename, input_device_index=11, chunk=1024, 
                            sample_format=pyaudio.paInt16, channels=1, 
                            rate=16000, seconds=3):

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
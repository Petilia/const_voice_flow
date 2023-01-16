from speeckit_tools import asr_from_yandex_speeckit

counter = 0
ogg_name = "ogg_file.ogg"

FOLDER_ID = "b1gami13b761380nb5hb" # Идентификатор каталога
API_KEY = "AQVN3XofRyHEW5PJOhBYCiObnGaZNYM8IvAQskdp" # API-ключ

asr_result = asr_from_yandex_speeckit(ogg_name, FOLDER_ID, API_KEY)
print(asr_result)
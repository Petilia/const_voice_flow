from speeckit_tools import tts_from_yandex_speechkit
import os

# Определяем, под каким индексом наш микрофон
FOLDER_ID = "b1gami13b761380nb5hb" # Идентификатор каталога
API_KEY = "AQVN3XofRyHEW5PJOhBYCiObnGaZNYM8IvAQskdp" # API-ключ

comands_dict = {"1" : "Вы подошли вплотную к роботу", 
                "2" : "Я окружен людьми",
                "3" : "Пожалуйста уступите дорогу роботу",
                "4" : "Не могу начать движение я окружен людьми",
                "5" : "Не могу продолжить движение"}


base_snippets_folder = "/home/appuser/py_files/snippets/"


for number, comand in comands_dict.items():
    tts_ogg_name = f"{number}.ogg"
    tts_ogg_name = base_snippets_folder + tts_ogg_name
    print(tts_ogg_name)
    # tts_ogg_name = os.path.join(base_snippets_folder, tts_ogg_name)

    tts_from_yandex_speechkit(comand, FOLDER_ID, API_KEY, tts_ogg_name=tts_ogg_name)
from speeckit_tools import tts_from_yandex_speechkit
import os

def remove_files_in_folder(folder_path):
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)
        print("mkdir folder")
    else:
        for f in os.listdir(folder_path):
            os.remove(os.path.join(folder_path, f))

def create_folder(folder_path):
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)
        print("mkdir folder")

def generation_by_speechkit(folder_path, comands_dict, 
                            FOLDER_ID = "b1gami13b761380nb5hb", 
                            API_KEY = "AQVN3XofRyHEW5PJOhBYCiObnGaZNYM8IvAQskdp"):

    for number, comand in comands_dict.items():
        tts_ogg_name = f"{number}.ogg"
        tts_ogg_name = folder_path + tts_ogg_name    
        tts_from_yandex_speechkit(comand, FOLDER_ID, API_KEY, tts_ogg_name=tts_ogg_name)

various_comands_dict = {"1" : "Вы подошли вплотную к роботу", 
                "2" : "Я окружен людьми",
                "3" : "Пожалуйста уступите дорогу роботу",
                "4" : "Не могу начать движение я окружен людьми",
                "5" : "Не могу продолжить движение",
                "6" : "Вы подошли ко мне сзади"}

n_people_comands_dict = {"0" : "Я не вижу людей",
            "1" : "Я вижу 1 человека",
            "2" : "Я вижу 2 человек",
            "3" : "Я вижу 3 человек",
            "4" : "Я вижу 4 человек",
            "5" : "Я вижу 5 человек",
            "6" : "Я вижу 6 человек",
            "7" : "Я вижу 7 человек",
            "8" : "Я вижу 8 человек",
            "9" : "Я вижу 9 человека",
            "10" : "Я вижу 10 человек",
            "11" : "Я вижу много людей"}

# Базовый путь к сниппетам
base_snippets_folder = "/home/appuser/py_files/snippets/"
# Путь к всяким сниппетам относительно того, что вокруг
various_folder = base_snippets_folder + "various/"
# Сниппеты относительно количества людей
n_people_folder = base_snippets_folder + "n_people/"

create_folder(base_snippets_folder)
remove_files_in_folder(various_folder)
remove_files_in_folder(n_people_folder)

generation_by_speechkit(various_folder, various_comands_dict)
generation_by_speechkit(n_people_folder, n_people_comands_dict)

# for number, comand in comands_dict.items():
#     tts_ogg_name = f"{number}.ogg"
#     tts_ogg_name = base_snippets_folder + tts_ogg_name
#     print(tts_ogg_name)
#     # tts_ogg_name = os.path.join(base_snippets_folder, tts_ogg_name)

#     tts_from_yandex_speechkit(comand, FOLDER_ID, API_KEY, tts_ogg_name=tts_ogg_name)
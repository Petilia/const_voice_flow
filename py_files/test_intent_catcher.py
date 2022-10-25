#!/usr/bin/env python

import requests
import json
from os import getenv

tests = [
    {
        "sentence": "Детектируй человека",
        "intent": "track_object"
    },
    {
        "sentence": "Повернись налево на 20 градусов",
        "intent": "turn_around"
    },
    {
        "sentence": "Пожалуйста проеди вперед 20 метров",
        "intent": "move_forward"
    },
    {
        "sentence": "Робот, проедь назад 20 метров",
        "intent": "move_backward"
    }
]


def main_test():
    url = "http://0.0.0.0:8014/detect"
    
    for test in tests:
        r = requests.post(url=url, json={"sentences": [[test["sentence"]]]})
       
        data = r.json()[0]
        print('=============')
        print(data)
 

if __name__ == "__main__":
    main_test()

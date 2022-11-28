import requests

number = 1
post_response = requests.get(f"http://localhost:8000/tts/{number}")

number = 0
post_response = requests.get(f"http://localhost:8000/tts_n_people/{number}")

number = 5
post_response = requests.get(f"http://localhost:8000/tts_n_people/{number}")

number = 10
post_response = requests.get(f"http://localhost:8000/tts_n_people/{number}")

number = 100
post_response = requests.get(f"http://localhost:8000/tts_n_people/{number}")

print('ok')
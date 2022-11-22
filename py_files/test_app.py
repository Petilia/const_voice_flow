import requests

number = 1
post_response = requests.get(f"http://localhost:8000/tts/{number}")

print('ok')
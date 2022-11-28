from fastapi import FastAPI
import os
import uvicorn
from pyaudio_tools import play_audio, get_device_index


index_device = get_device_index()

app = FastAPI()

@app.get("/tts/{number}")
async def create_item(number:str):
    wav_name = f"/home/appuser/py_files/snippets/various/{number}.wav"
    if os.path.isfile(wav_name):
        play_audio(wav_name, index_device)

@app.get("/tts_n_people/{number}")
async def create_item(number:str):
    if int(number) <= 10:
        wav_name = f"/home/appuser/py_files/snippets/n_people/{number}.wav"
        if os.path.isfile(wav_name):
            play_audio(wav_name, index_device)
    else:
        wav_name = f"/home/appuser/py_files/snippets/n_people/11.wav"
        if os.path.isfile(wav_name):
            play_audio(wav_name, index_device)    


if __name__ == "__main__":
    uvicorn.run("app:app", port=8000)
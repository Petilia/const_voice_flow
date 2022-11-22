from fastapi import FastAPI
import os
import uvicorn
from pyaudio_tools import play_audio, get_device_index


index_device = get_device_index()

app = FastAPI()

@app.get("/tts/{number}")
async def create_item(number:str):
    wav_name = f"/home/appuser/py_files/snippets/{number}.wav"
    if os.path.isfile(wav_name):
        play_audio(wav_name, index_device)

if __name__ == "__main__":
    uvicorn.run("app:app", port=8000)
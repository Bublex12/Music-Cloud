import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from database import get_info_sound_in_database



app = FastAPI()


# Получить список всех аудиофайлов в папке audio
def get_audio_files():
    audio_folder = "../static/audio"
    audio_files = []
    for filename in os.listdir(audio_folder):
        if filename.endswith(".mp3"):
            audio_files.append(filename)
    return audio_files


templates = Jinja2Templates(directory=os.path.join(os.path.dirname(os.path.abspath(__file__)), "../templates"))


@app.get("/audio", response_class=HTMLResponse)
async def get_all_audio(request: Request):
    audio_files = get_audio_files()
    return templates.TemplateResponse("index.html", {"request": request, "audio_files": audio_files})


@app.get("/audio/{filename}", response_class=FileResponse)
async def get_audio(filename: str):
    audio_folder = "../static/audio"
    audio_path = os.path.join(audio_folder, filename)
    return audio_path


@app.get("/audio/info/{filename}")
async def get_info_audio(filename: str):
    audio_folder = "../static/audio"

    id_sound = str(filename.split('.')[0])

    return get_info_sound_in_database(id_sound)
import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from database import get_info_sound_in_database
from fastapi.staticfiles import StaticFiles
from pathlib import Path




app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)
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
    info_sound_list = []
    for audio_file in audio_files:
        id_sound = str(audio_file.split('.')[0])
        info_sound_list.append(get_info_sound_in_database(id_sound))
    print(info_sound_list)
    return templates.TemplateResponse("index.html", {"request": request, "audio_files": audio_files, "sound_info_list": info_sound_list})


@app.get("/audio/{filename}", response_class=FileResponse)
async def get_audio(filename: str):
    audio_folder = "../static/audio"
    audio_path = os.path.join(audio_folder, filename)
    return audio_path

@app.get("/audio/img/{filename}", response_class=FileResponse)
async def get_img(filename: str):
    img_folder = "../static/img"
    img_path = os.path.join(img_folder, filename+'.jpg')
    return img_path



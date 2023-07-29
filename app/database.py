from config import get_connection_test
import os

def get_info_sound_in_database(id_sound: str):
    con = get_connection_test()
    cur = con.cursor()
    cur.execute(f'SELECT id,song_name, artist, album FROM public.info_sound WHERE id = {id_sound}')
    info_sound = cur.fetchall()
    # info_sound_array = []
    # id = str(info_sound[0][0])
    # song_name = info_sound[0][1]
    # artist = info_sound[0][2]
    # album = info_sound[0][3]
    # img_folder = "../static/img"
    # img_name = id + '.jpg'
    # img_path = os.path.join(img_folder, img_name)
    # info_sound_array = [id, song_name, artist, album, img_path]
    print(info_sound)
    return info_sound



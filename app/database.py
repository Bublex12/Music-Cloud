from config import get_connection_test
import os

def get_info_sound_in_database(id_sound: str):
    con = get_connection_test()
    cur = con.cursor()
    cur.execute(f'SELECT id,song_name, artist, album FROM public.info_sound WHERE id = {id_sound}')
    info_sound = cur.fetchall()

    print(info_sound)
    return info_sound



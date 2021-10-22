from playsound import playsound
import glob
import os

home_drive = os.getenv('HOMEDRIVE')
home_path = os.getenv('HOMEPATH')

files_path = rf'{home_drive}{home_path}\Music\*.mp3'

musics = glob.glob(f'{files_path}')

reproduce = lambda music: playsound(music)

for music in musics:
    reproduce(music)

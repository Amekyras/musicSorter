import eyed3
import glob
import re
import os
import shutil
from pathlib import Path

filelist = glob.glob("*.mp3", recursive=False)

for x in range(0, len(filelist)):
    curfile = eyed3.load(filelist[x])
    rawartist = curfile.tag.album_artist
    rawalbum = curfile.tag.album
    artist = re.sub(r"[\\/:*?\"<>|]+", " ", rawartist)
    album = re.sub(r"[\\/:*?\"<>|]+", " ", rawalbum)
    dirpath = os.path.join(artist, album)
    if Path.is_dir(Path(dirpath)) is False:
        os.makedirs(dirpath)
    pathfile = os.path.join(dirpath, filelist[x])
    shutil.move(filelist[x], pathfile)

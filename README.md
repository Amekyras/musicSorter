The Plan
-
pathlib library

use eyeD3 to handle metadata

Get list of all .mp3 files in folder - fnmatch

for x in range (1, list)

read metadata of file

move file to a folder named after its artist, create if necessary

move file to a folder named after its album, create if necessary

continue to next file

commands needed:

os.listdir() - gets contents of current dir as list of strings

os.makedirs("./artist/album") - mkdir

shutil.move("srcpath", "destpath")

os.path.join("artistname", "albumname", "songname.ext") - makes a path! feed it to mkdirs!
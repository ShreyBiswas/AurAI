# get number of files in musicxml folder
import os
from random import sample

music_xml_files = os.listdir('musicxml')
print(len(music_xml_files))
# sample 10 from musicxml files
sample_files = sample(music_xml_files, 10)
print(sample_files)

def clear(folder_name):
    # delete all files in folder
    filelist = os.listdir(folder_name)
    for f in filelist:
        os.remove(os.path.join(folder_name, f))

clear('sample')

# copy first 10 files to new folder
import shutil
def copy():
    for i in range(10):
        # copy file from musicxml folder to sample folder
        shutil.copy(f'./musicxml/{sample_files[i]}', './sample/')

copy()
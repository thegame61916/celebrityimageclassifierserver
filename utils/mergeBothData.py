import scipy.io 
import os
from shutil import copyfile
import shutil
import numpy as np
import glob


path_imdb = "/Users/mohit.sh/Downloads/results copy/"
path_mic = "/Users/mohit.sh/Downloads/dataset3 copy/"

imdb_folders = [x[0] for x in os.walk(path_imdb)][1:]
mic_folders = [x[0] for x in os.walk(path_mic)][1:]
imdb_names = []
mic_names = []
for f in imdb_folders:
    imdb_names.append(f.split('/')[-1].split(',')[0])

for f in mic_folders:
    mic_names.append(f.split('/')[-1].split(',')[0])


for f in mic_names:
        if f in imdb_names:
                src = imdb_folders[imdb_names.index(f)]
                dest = mic_folders[mic_names.index(f)]
                if(src.split('/')[-1] != dest.split('/')[-1]):
                        os.makedirs("/Users/mohit.sh/Downloads/dataset3 copy/" + src.split('/')[-1])
                        for g in glob.glob(os.path.join(src, "*.jpg")):
                                shutil.copy(g, "/Users/mohit.sh/Downloads/dataset3 copy/" + src.split('/')[-1])

                        for g in glob.glob(os.path.join(dest, "*.jpg")):
                                shutil.copy(g, "/Users/mohit.sh/Downloads/dataset3 copy/" + src.split('/')[-1])
                        shutil.rmtree(dest)
                        shutil.rmtree(src)
                else:
                        for g in glob.glob(os.path.join(src, "*.jpg")):
                                if(os.path.exists(dest + "/" + g.split('/')[-1])):
                                        pass
                                else:
                                        shutil.copy(g, dest)
                        shutil.rmtree(src)

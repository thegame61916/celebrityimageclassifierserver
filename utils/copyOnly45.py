import scipy.io 
import os
from shutil import copyfile
import shutil
import numpy as np
import glob


path = "/Users/mohit.sh/Desktop/projectFace/dlib-master/python_examples/dataset4"
folders = [x[0] for x in os.walk(path)][1:]
j = 0
for f in folders:
        os.makedirs("/Users/mohit.sh/Desktop/projectFace/dlib-master/python_examples/copy/" + f.split('/')[-1])
        i =0
        for g in glob.glob(os.path.join(f, "*.jpg")):
            shutil.copy(g, "/Users/mohit.sh/Desktop/projectFace/dlib-master/python_examples/copy/" + f.split('/')[-1])
            i = i + 1
            if(i>=44):
                break
        print(f)
        print(j)
        j = j +1

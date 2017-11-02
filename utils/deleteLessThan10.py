import shutil 
import os
from shutil import copyfile
import sys
import glob

def checkAndDelete(path):
        # Now process all the images
        l = []
        for f in glob.glob(os.path.join(path, "*.jpg")):
                l.append(f)
        if(len(l)<=40):
                shutil.rmtree(path)
                
allFolders = [x[0] for x in os.walk(sys.argv[1])][1:]
for f in allFolders:    
    checkAndDelete(f)

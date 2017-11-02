#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 13:22:44 2017

@author: archit.j
"""

import os

counter = 0
def changeFoldersLabelToNumbers(path):
        global  counter
        newFileName = "/Users/mohit.sh/Desktop/dataset4/" + str(counter)
        print path
        print newFileName
        os.rename(path, newFileName)
        counter = counter +1
     
    

        
allFolders = [x[0] for x in os.walk("/Users/mohit.sh/Downloads/dataset3 copy")][1:]
allFolders.sort()

#print allFolders

#for f in allFolders:
 #   findDescriptorsInFolder(f)
    


for x in allFolders:
    changeFoldersLabelToNumbers(x)

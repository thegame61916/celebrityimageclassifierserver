import os

path="dataset3"
id = 0
dct = {}

allFolders = [x[0] for x in os.walk(path)][1:]
for f in allFolders:
        dct[id] = {}
        dct[id]['name'] = f.split(',')[0].split('/')[1]
        dct[id]['age'] = f.split(',')[1]
        dct[id]['gender'] = f.split(',')[2]
        dct[id]['file'] = path + '/' + os.listdir(f)[0]
        id = id + 1
print(dct)

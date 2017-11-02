import scipy.io 
import os
from shutil import copyfile
import numpy as np

PATH="/Users/mohit.sh/Downloads/imdb_crop/"
mat=scipy.io.loadmat('/Users/mohit.sh/Downloads/imdb_crop/imdb.mat')['imdb'][0][0]
n=len(mat[4][0])
dic={}
for j in range(n):
	if len(mat[4][0][j])==0:
		continue
	key=mat[4][0][j][0].split(' \ ')[0]
	print(key)
	if(key in dic):
		prev=dic[mat[4][0][j][0]]['age']
		new=mat[1][0][j]-mat[0][0][j]/365
		print(prev)
		print(new)
		if(new > prev):
                        print(new)
                        dic[mat[4][0][j][0]]['age']=new
		dic[mat[4][0][j][0]]['link'].append(mat[2][0][j])
	else:		
		dic[mat[4][0][j][0]]={}
		dic[mat[4][0][j][0]]['age']=mat[1][0][j]-mat[0][0][j]/365
		if mat[3][0][j]==1:
			dic[mat[4][0][j][0]]['gender']='MALE'
		else:
			dic[mat[4][0][j][0]]['gender']='FEMALE'
		dic[mat[4][0][j][0]]['link']=[]
		dic[mat[4][0][j][0]]['link'].append(str(mat[2][0][j][0]))

if not os.path.exists("./results"):
	os.makedirs("./results")
for key in dic:
	path="./results/"
	if not os.path.exists(path +key + ',' + str(dic[key]['age']) + ',' +dic[key]['gender']):
		os.makedirs(path +key + ',' + str(dic[key]['age']) + ',' +dic[key]['gender'])
	lis=dic[key]['link']
	for y in lis:
		x=y
		print x
		if isinstance(y, (np.ndarray, np.generic) ):
			x=x[0]
		copyfile(str(PATH) + str(x) ,path +key + ',' + str(dic[key]['age']) + ',' +dic[key]['gender'] + '/' + x.split('/')[1] )

		#print(dic[mat[4][0][j][0]]['age'])
	#!---:[{'age':mat[1][0][j]-mat[0][0][j]/365,'gender':mat[3][0][j],'link':mat[2][0][j]}]]

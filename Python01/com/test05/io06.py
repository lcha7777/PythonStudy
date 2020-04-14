# -*- coding:utf-8 -*-


import pickle
from html.parser import piclose

file=open('test02.txt','rb')

score=pickle.load(file)

print(score)
file.close()
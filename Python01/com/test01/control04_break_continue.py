# -*- coding:utf-8 -*-
from ntpath import sep

i = 1
while i <= 10:
    if i > 5:
        break
    print(i)
    i += 1
else:
    print('i:'+str(i))#???break때문에 실행x?

print()

for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)
else:
    print('i',i,sep=':')#/?????????













# -*- coding:utf-8 -*-

n = input('n 입력:')

print(n)

a,b=0,1
i=0

while i<int(n):
    print(a,end=' ')
    a,b = b,a+b
    i+=1
    
    
print()
    
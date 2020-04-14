# -*- coding:utf-8 -*-
from math import factorial

#함수 안에서 함수 자기자신을 호출하는 방식을 재귀호출(recursive call)이라고 합니다. 
def factorial(n):
    
    res=1
    for i in range(1,n+1):
        res*=i
        
        
    return res
     


def factorialRecursion(n):
    
    if n ==1:
        
        return 1
    return n * factorialRecursion(n-1)
'''
return 5*
     return  4*
          return3*
              return2*
                    return


'''



if __name__ == '__main__':
    n = int(input('n:'))
    
    res = factorialRecursion(n)
    
    print('{} factorial={}'.format(n    , res))
    print('{} factorial={}'.format(n    , factorial(n)))

 
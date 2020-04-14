# -*- coding:utf-8 -*-


def hello(count):
    
   if count==0:
       return 
   
   
   print('Hello, world',count)
   
   count-=1
   
   hello(count)
    
   '''
   def factorial(n):
    
    if n ==1:
        
        return 1
    
    return n * factorial(n-1)
   
   
   ''' 
    
    
    



if __name__ == '__main__':
    hello(5)


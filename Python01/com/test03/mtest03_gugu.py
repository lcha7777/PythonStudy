# -*- coding:utf-8 -*-

# 1. for문을 사용하여 구구단 전체를 출력하는 gugu() 함수를 만들자.
def gugu():
    print('구구단')
    for i in range(2, 10):
        print('<<< {}단 >>>'.format(i))
        for j in range(1, 10):
            print('{} * {} = {}'.format(i, j, i * j))


# 2. while문을 사용하여 입력된 숫자의 단만 출력하는 gugudan(x)를 만들자.
def gugudan(x):
    print(str(x)+'단')
    i = 1
    while i < 10:
        print('{} * {} = {}'.format(x, i, x * i))
        i += 1

# 3. main 만들어서 위의 두 함수를 호출하자.
if __name__ == '__main__':
    gugu()
    dan = int(input('단을 입력해 주세요 : '))
    gugudan(dan)
    
    
    
    
    
    
    
    
    
    
    
    








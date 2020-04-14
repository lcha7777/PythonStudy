# -*- coding:utf-8 -*-

subject = ['java', 'javascript', 'python']

for i in subject:
    print(i)



for i in subject:
    print(i, end=' ')#?? # end에 빈 문자열을 지정하면 다음 번 출력이 바로 뒤에 오게 됨
else:
    print('\n재밌다.')#?? for문이 중간에 break 등으로 끊기지 않고,끝까지 수행 되었을 때 수행하는 코드를 담고 있습니다.


for i in range(1, 100):
    print(i, end=', ')
else:
    print(100)

print('----------')




print('<<구구단>>')
for i in range(2, 10):
    print('<'+str(i)+'단>')
    for j in range(1, 10):
        print(i,'*',j,'=',(i * j), sep=' ')
print()

for i in range(10,0,-1):
    print(i)














# -*- coding:utf-8 -*-
#https://api.mongodb.com/python/current/tutorial.html 까 먹으면 들어가서 과정 보기
from pymongo import MongoClient
import pprint

client = MongoClient('localhost',27017)
 
db = client.test
score= db.score

cursor = score.find()
print(cursor)

for doc in cursor:
    pprint.pprint(doc)
    
    
print("-------------")
hong=score.find({'name':'홍길동'})

pprint.pprint(hong)

for doc in hong:
    print(doc)

print("------------------------")
cho = score.find_one({'name':'조세호'})#find:몇개를 찾는지 몰라서 주소가 나오고 find_one은 한개 전체가 나온다.
pprint.pprint(cho)

print("------------------------")
print('document의 총 갯수:',score.count_documents({}))

#국어 점수가 70보다 높은 사람만 출력하자.
kor = score.find({'kor':{'$gt':70}})
print(kor)

for doc in kor:
    print(doc)
    





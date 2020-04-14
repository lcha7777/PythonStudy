# -*- coding:utf-8 -*-

from pymongo import MongoClient
client = MongoClient('localhost',27017)

db=client.test
score =db['score']

res01 = score.insert_many([
    {
        'name':'박선우',
        'midterm':{'kor':100,'eng':70,'math':80},
        'final':{'kor':90,'eng':40,'math':100}
        },
    
    {
        'name':'이지애',
        'midterm':{'kor':100,'eng':90,'math':80},
       
        }
            
])


print(res01.inserted_ids)

res02 = db.score.insert_one(
    
    {'name':'데드풀','kor':100,'eng':100}
    
    
)

print(res02.inserted_id)





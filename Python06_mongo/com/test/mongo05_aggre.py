# -*- coding:utf-8 -*-

from pymongo import MongoClient
import pprint
client = MongoClient('localhost',27017)

db = client.test
score= db.score

aggr = score.aggregate([
    
   {'$match':{'kor':{'$gt':50}}},
   {'$group':{'_id':'kor','sum':{'$sum':'$kor'}}}    #합친다 국어 점수의 총 합을 /50보다 큰 아이들의    
    
])

print(aggr)#command_cusor/mongodb-server-python

pprint.pprint(list(aggr))






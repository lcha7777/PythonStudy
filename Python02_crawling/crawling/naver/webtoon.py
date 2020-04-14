# -*- coding:utf-8 -*-

#pip install requests

import requests
from bs4 import BeautifulSoup
import json

resp = requests.get('https://comic.naver.com/webtoon/weekdayList.nhn?week=wed')

soup = BeautifulSoup(resp.text,'html.parser')
#print(soup)


webtoon_list = soup.find('ul', class_='img_list')
#print(webtoon_list)

dl=webtoon_list.select('dl')
'''중간에 들어가있는 태그 쓰기'''

lst=list()

for chd in dl:
    title = chd.find('a').text
    #title = chd.select('a')[0]
    star = chd.find('strong').text
    
    '''
    {webtoon:[{title:제목},...]}
    
    '''

    tmp ={}
    tmp['title']=title
    tmp['star']=star
    
    '''{"title":"제목","start":"9.93"},...'''
   
    
    lst.append(tmp)
    #print(lst)  
res = {}
res['webtoons']=lst
print(lst)
res_json = json.dumps(res, ensure_ascii=False)
print(res_json)


#try(con,pstm){ 저절로 문이 닫힌다.}
with open('webtoon.json','w',encoding='utf-8') as file:
    file.write(res_json)






# -*- coding:utf-8 -*-



import requests
from bs4 import BeautifulSoup






resp = requests.get('https://comic.naver.com/webtoon/weekdayList.nhn?week=wed')

soup = BeautifulSoup(resp.text,'html.parser')

webtoon_list = soup.find('ul',class_='img_list' )


dl = webtoon_list.select('dl')

lst=list()

for chd in dl:
    #title=chd.find('a').text
    title=chd.select('a')[1].text
    print(title)


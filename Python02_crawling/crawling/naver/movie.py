# -*- coding:utf-8 -*-


#pip install beautifulsoup4



from bs4 import BeautifulSoup
import urllib.request

''' 
document는 string으로 넘어온다. 이걸 tag로 바꿔주는것이
beautifulsoup 이다.
'''

resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn?order=point#')
soup=BeautifulSoup(resp,'html.parser')#resp 문자열에 대해서 tag 로 파싱한다.

#print(soup)


movies = soup.find_all('dl', class_='lst_dsc')
#print(movies)


for movie in movies:
    title = movie.find('a').text
    star = movie.find('span',class_='num').text
   #print(title)
    print('{} [{}]'.format(title, star))
   


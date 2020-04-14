# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

import requests


tag=input('search tag:')
url='https://www.instagram.com/explore/tags/'+tag

resp = requests.get(url)
soup=BeautifulSoup(resp,'html.parser')
#print(soup)

print(soup.find('div',class_='KL4Bh'))











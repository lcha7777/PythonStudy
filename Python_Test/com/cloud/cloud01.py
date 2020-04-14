# -*- coding:utf-8 -*-


#pip install wordcloud

from wordcloud import WordCloud
import json

cloud = WordCloud(font_path='Goyang.ttf',background_color='white'
                  ,max_words=30,width=400,height=300)

with open('webtoon.json','r', encoding='utf-8') as file:
    
    webtoon = json.load(file)
    #print(webtoon)
    
    
res = dict()
for tmp in webtoon['webtoons']:
    
    res[tmp['title']] = int(float(tmp['star'])*100)
    
    #{'유미의 세포들':980}
    
visual = cloud.fit_words(res)

visual.to_image()
visual.to_file('cloud.png')


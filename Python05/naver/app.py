# -*- coding:utf-8 -*-






from flask import Flask,render_template#render_template 파일을 리턴할떄 사용
import requests
from bs4 import BeautifulSoup
import json 
import urllib
#pip install flask_cors : cross origin(정체기) 자바 스크립트로 요청해서 응답하는 데이터는 같은 서버에 있자. 플라스크 tomcat client client/ jsonp 찾아서 해결 하자/ 
import flask_cors   #API(Application Programming Interface)

app=Flask(__name__)
flask_cors.CORS(app)

@app.route('/')
def root():
    
    return render_template('index.html')

@app.route('/crawling')
def crawling():
    #naver movie list를 crawling 해오자
    #crawling 된 데이터를 [{title:제목 star:별점.....}] 로 저장하자.
    #json으로 변환하여 리턴하자.
    
    resp = requests.get('https://movie.naver.com/movie/running/current.nhn?order=point#')
    soup = BeautifulSoup(resp.text,'html.parser')#html.parser: beautifulsoup 홈페이지에서 api 찾아보기 파이썬 주고 있는 기본적인 parser이다.
    
    movies = soup.find_all('dl',class_='lst_dsc')
    
    result = list()
    for movie in movies:
    
        tmp =dict()
        
        tmp['title']=movie.find('a').text
        
        tmp['star']=movie.select('.num')[0].text
    
        result.append(tmp)
    
    res_dict={'movies':result}
    
    #json으로 변환하여 리턴하자.
    api=json.dumps(res_dict,ensure_ascii=False)
    
    return api
    
    
    
    
    '''
    resp = requests.get('https://movie.naver.com/movie/running/current.nhn?order=point#')
    soup = BeautifulSoup(resp.text,'html.parser')#html.parser: beautifulsoup 홈페이지에서 api 찾아보기 파이썬 주고 있는 기본적인 parser이다.
    
    movie_list=soup.find_all('dl',class_='lst_dsc')
    #dl =movie_list.select('dl')
    
    lst=list()
    
    for chd in movie_list:
        title = chd.find('a').text
        star = chd.find('span',class_='num').text
        
        
        tmp={}
        tmp['title']=title
        tmp['star']=star
        
        lst.append(tmp)
        
    res={}
    res['movies']=lst
    res_json = json.dumps(res, ensure_ascii=False)
        
    return render_template('list.html',list=res_json)
    '''
    
if __name__ =='__main__':
    app.run('localhost', port='8585')   


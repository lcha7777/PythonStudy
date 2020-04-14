# -*- coding:utf-8 -*-

#Flask는 Python으로 구동되는 웹 어플리케이션 프레임워크

from flask import Flask

app = Flask(__name__) #flask의 인스턴스를 생성



@app.route('/')  #URL MAPPING 
def hello():
    
    return "Hello, Flask!"

if __name__=='__main__':#자바에서 main method
    app.run()


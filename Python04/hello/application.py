# -*- coding:utf-8 -*-

#진자 사용 controller  역할을 한다.
'''

application  controller
template html
static  css js

'''

from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def root():
    
    return '''
            <a href="/hello">hello</a><br>
                <input type ="button" value="hello" 
                onclick="location.href='/hello/name'"/>
            
    
    '''
@app.route('/hello')   
@app.route('/hello/<name>') 
def hello(name=None): 
    
    return render_template('hello.html', name=name)






@app.route('/test',methods=['post'])
def test():
    
    return render_template('test.html',test=request.form['command'])














if __name__=='__main__':
    app.run('localhost',port='8585')








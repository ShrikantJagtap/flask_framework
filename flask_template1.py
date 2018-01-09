'''
Created on Jan 9, 2018

@author: shrikant_jagtap
'''
from flask.app import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def get_hello():
    user = {"username":"shri"}
    return render_template('index.html', title='Home', user=user)
    

if __name__ == '__main__':
    app.run('ip_address')

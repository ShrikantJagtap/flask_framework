'''
Created on Jan 9, 2018

@author: shrikant_jagtap
'''

import flask
from flask.app import Flask

app = Flask(__name__)

@app.route("/hello")
def get_hello():
    return "hello flask"


if __name__ == '__main__':
    app.run('ip')

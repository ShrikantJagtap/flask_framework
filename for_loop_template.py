'''
Created on Jan 9, 2018

@author: shrikant_jagtap
'''

from flask import render_template
from flask.app import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'shri'}
    skills = [
        {
            'name': 'python',
            'body': 'python body'
        },
        {
            'name': 'flask',
            'body': 'flask body'
        }
    ]
    return render_template('index.html', title='Home', user=user, skills=skills)

if __name__ == '__main__':
    app.run('ip_address')

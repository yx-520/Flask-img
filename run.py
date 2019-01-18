# -*- encoding:utf8 -*-
from flask import Flask
# from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Mixi paradise!'

if __name__ == '__main__':
    app.run()
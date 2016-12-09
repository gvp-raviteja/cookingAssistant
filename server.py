__author__ = 'hemalatha_ganireddy'

import os
from flask import Flask, request
import sys

import main
import json

app = Flask(__name__)

@app.route('/favicon.ico')
def sam():
    return True

@app.route('/',methods=['GET'])
def index():
    
    # json.loads(output)['result']['metadata']['intentName']
    return "Hello, World!"

@app.route('/',methods=['POST'])
def index1():
    print request.form['data']
    # json.loads(output)['result']['metadata']['intentName']
    return request.form['data']

if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

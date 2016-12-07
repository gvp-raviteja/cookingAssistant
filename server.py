__author__ = 'hemalatha_ganireddy'

import os
from flask import Flask
import sys

import main
import json

app = Flask(__name__)

@app.route('/favicon.ico')
def sam():
    return True

@app.route('/')
def index():
    # output = main.ma()
    # json.loads(output)['result']['metadata']['intentName']
    return "Hello, World!"

port = int(os.environ.get("PORT", 5000))
app.run(debug=True, port=port)

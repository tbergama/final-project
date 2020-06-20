from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import os
import pymongo
from bson.json_util import dumps
import json


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



# Run app
if __name__ == '__main__':
    app.run(debug=True)
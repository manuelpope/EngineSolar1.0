from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

import json, os




def processJsonReader(pathProp = ""):
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, pathProp)
    with open(filename, 'r') as f:
        dictLoad = json.load(f)
    return dictLoad
dictProp = processJsonReader("properties.json")
# initializations
app = Flask(__name__)
# Mysql Connection
app.config['MYSQL_HOST'] = dictProp.get('MYSQL_HOST')
app.config['MYSQL_USER'] = dictProp.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = dictProp.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = dictProp.get('MYSQL_DB')
mysql = MySQL(app)
# settings
app.secret_key = "mysecretkey"

from controller.Controller import  *
if __name__=='__main__':
    app.run(port='8000',debug=True)

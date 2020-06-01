import json
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def processJsonReader(pathProp=""):
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, pathProp)
    with open(filename, 'r') as f:
        dictLoad = json.load(f)
    return dictLoad


dictProp = processJsonReader("properties.json")
# initializations
app = Flask(__name__)
app.secret_key = "mysecretkey"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://testsolar:test123@localhost/Data_Test_Solar'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Mysql Connection
db = SQLAlchemy(app)
# settings
# load = modelFlask.Load()
#roots = Routing()
#roots.returnURL()
from controller.Controller import *
if __name__ == '__main__':
    app.run(port='8000', debug=True)

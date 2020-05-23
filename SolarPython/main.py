from flask import Flask, render_template, request, redirect, url_for, flash
#from flask_mysqldb import MySQL
import json

# initializations
app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Adali1392'
app.config['MYSQL_DB'] = 'invernadero001'
#mysql = MySQL(app)


def processJsonReader(pathProp = ""):
    with open(pathProp, 'r') as f:
        pathProp.dictLoad = json.load(f)
    return pathProp.dictLoad
# settings
app.secret_key = "mysecretkey"
dictProp = {}
dictProp = processJsonReader("/Users/manueltobon/Desktop/EngineSolar1.0/EngineSolar1.0/SolarPython/properties.json")
for x in dictProp:
    print(dictProp.get("prop").get(x))

if __name__=='__main__':

    app.run(debug=True)
from flask import Flask
from flask_restful import Api

import controller.Resources
from db import db

# initializations


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://testsolar:test123@localhost/Data_Test_Solar'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
app.config['expire_on_commit'] = False

app.secret_key = 'manu'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(controller.Resources.LoadResource, '/load/<string:designId>')
api.add_resource(controller.Resources.LoadList, '/loadlist')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"

# SqlAlchemy Database Configuration With Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://testsolar:test123@localhost/Data_Test_Solar'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Creating model table for our CRUD database
class Load(db.Model):
    __tablename__ = "LOAD"
    id = db.Column(db.Integer, primary_key=True)
    __voltage = db.Column('voltage', db.String(100))
    current = db.Column(db.String(100))
    pf = db.Column(db.String(100))
    workingHours = db.Column(db.String(100))
    typeL = db.Column(db.String(100))

    def __init__(self, vx=0, current=0, hours=0):
        self.vx = vx
        self.current = current
        self.workingHours = hours

    @property
    def vx(self):
        return self.__voltage

    @vx.setter
    def vx(self, vx):
        if float(vx) > 500:
            self.__voltage = 100
        else:
            self.__voltage = float(vx)


# This is the index route where we are going to
# query on all our employee data
@app.route('/')
def Index():
    load = Load()
    load.current = 5
    load.vx = 100000000
    load.__voltage = 6
    load.pf = 45
    load.workingHours = 6.6
    load.typeL = "DC"
    load2 = Load(5.6, 5, 5)
    db.session.add(load2)
    db.session.add(load)
    db.session.commit()
    flash("Employee Inserted Successfully")
    all_data = Load.query.all()
    for x in all_data:
        print(x.vx)
    return render_template("index.html", data=all_data)


if __name__ == "__main__":
    app.run(debug=True)
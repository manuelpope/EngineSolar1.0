from flask import render_template, flash

from adapter.model.modelFlask import Load
from app import app, db


@app.route('/')
def index():
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

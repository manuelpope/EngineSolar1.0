import flask
from flask import flash, request, redirect, url_for

from adapter.model.modelFlask import Load
from app import app, db


def serialize(group):
    rjson = {}
    x = 0
    for reg in group:
        x += 1
        rjson[x] = str(reg)
        print(x, reg)
    # print(rjson, len(group))
    return rjson


@app.route('/')
def index():
#   load = Load()
#    load.current = 5
#    load.vx = 100000000
 #   load.__voltage = 6
  #  load.pf = 45
   # load.workingHours = 6.6
    #load.typeL = "DC"
    #load2 = Load(5.6, 5, 5)
    #db.session.add(load2)
    #db.session.add(load)
    #db.session.commit()
    #flash("Employee Inserted Successfully")
    #all_data = Load.query.all()

    #r2json = serialize(all_data)
    #return (flask.render_template('form.html'), r2json)
    return (flask.render_template('form.html'))


@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        flash('Contact Updated Successfully')
        return redirect(url_for('Index'))


@app.route('/delete/<string:id>', methods=['POST', 'GET'])
def delete_contact(id):
    flash('Contact Removed Successfully')
    return redirect(url_for('Index'))


@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        flash('Contact Added successfully')
        return redirect(url_for('Index'))

@app.route('/sign-up', methods=['POST'])
def loadReceive():
    dict= request.form
    for k,v in dict.items():
        print(k," : ",v)
    flash('Load Added successfully')
    return redirect(('/'))

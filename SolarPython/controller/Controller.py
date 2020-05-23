from main import app
from flask import render_template
from adapter.worker.Technichian import Technichian

@app.route('/')
def index():
    tech = Technichian()
    tech.work()
    print("Calcs Done")
    return render_template('index.html')


from flask import render_template
from app import app

@app.route('/area_logada')
def area_logada():
    return render_template('area_logada.html')
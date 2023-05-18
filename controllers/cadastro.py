from flask import render_template, redirect, request
from app import app

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')
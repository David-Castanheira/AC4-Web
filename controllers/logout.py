from flask import render_template, redirect, request
from app import app 

@app.route('/logout')
def logout():
    return redirect('login.html')
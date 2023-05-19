from flask import Flask, redirect
from app import app 

app = Flask(__name__)

@app.route('/logout')
def logout():
    return redirect('login.html')
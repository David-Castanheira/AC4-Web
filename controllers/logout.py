from flask import redirect
from app import app 

@app.route('/logout')
def logout():
    return redirect('login.html')
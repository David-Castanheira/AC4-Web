from flask import Flask


app = Flask(__name__)
app.secret_key = b'09c5ddd8fb2311edbe1990b11cf6128c'

from controllers import *

if __name__ == '__main__':
    app.run(debug=True)
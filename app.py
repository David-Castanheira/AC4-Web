from flask import Flask

app = Flask(__name__, template_folder='templates')

# Adicionar chave secreta para usar nas sessões 

from controllers import *

# Lista de usuários usuarios = []

app.run(debug=True)
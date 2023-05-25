from flask import Flask

app = Flask(__name__)

# Adicionar chave secreta para usar nas sessões 

from controllers import *

# Lista de usuários usuarios = []

if __name__ == '__main__':
    app.run(debug=True)
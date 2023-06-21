from flask import render_template, request, session, redirect, url_for
from app import app


class Infos:
    def __init__(self, nome, email, telefone, assunto, mensagem, marketing):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.assunto = assunto
        self.mensagem = mensagem
        self.marketing = marketing


info = Infos("", "", "", "", "", "")

@app.route('/')
@app.route('/home')
def home():
    texto = ""
    if info.nome:
        texto = f'Seja bem-vindo, {info.nome}!'
    else:
        texto = 'Seja bem-vindo, visitante!'
    return render_template('home.html', texto=texto)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/confirmacao')
def confirmacao():
    if not info.nome or not info.email:
        return redirect('/home')
    return render_template('confirmacao.html', nome=info.nome, email=info.email, texto=f'Seja bem-vindo, {info.nome}!')

@app.route('/formulario', methods=['POST'])
def formulario():
    info.nome = request.form['nome']
    info.email = request.form['email']
    info.telefone = request.form['telefone']
    info.assunto = request.form['assunto']
    info.mensagem = request.form['mensagem']
    info.marketing = request.form['marketing']

    return redirect('/confirmacao')
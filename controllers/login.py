import uuid
from flask import render_template, redirect, request, session, make_response, url_for
from app import app 

@app.route('/login')
def login_get():
    return render_template('login.html')

usuario1 = {'login': 'gabriel', 'senha': 'bradesco123'}

@app.route('/login', methods=['POST'])
def login_post():
    print('form', request.form)
    usuario = request.form.get('email')
    senha = request.form.get('senha')

    if not usuario == usuario1['login']:
        return 'Usuário não encontrado'
    
    if not senha == usuario1['senha']:
        return 'Senha incorreta'
    
    dic_usuario = {'nome': usuario}

    id_sessao = str(uuid.uuid1())
    session.update({id_sessao: dic_usuario})

    print('sessão do servidor', session)
    resposta = make_response(redirect(url_for('area_logada')))
    resposta.set_cookie('session-id', id_sessao)
    resposta.set_cookie('teste', '123')

    return resposta
    
@app.route('/logout')
def logout():
    id_sessao = request.cookies.get('session-id')
    usuario = session.pop(id_sessao, None)

    if usuario is None:
        print('Usuário inexistente!')
    resposta = make_response(redirect(url_for('login_get')))
    resposta.set_cookie('sessio-id', '')

    return resposta
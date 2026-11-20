from estudos import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    nome = 'teste'
    context ={
        'nome': nome
    }
    return render_template('index.html', context=context)

@app.route('/teste/')
def teste1():
    return "teste"
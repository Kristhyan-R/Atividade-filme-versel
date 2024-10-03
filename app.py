from flask import Flask, render_template, request, redirect
lista = []

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('Home.html', Titulo1 = 'Bem vindo ao site de Filmes')


@app.route('/filme')
def filme():
    return render_template('Filme.html', Titulo2 = 'Lista de Gêneros de Filmes')


@app.route('/sobre')
def sobre():
    return render_template('Sobre.html', Titulo3 = 'Sobre o nosso site')


@app.route('/cadastro')
def cadastro():
    return render_template('Cadastro.html', Titulo4 = 'Cadastro de Filmes')

@app.route('/exibir')
def exibir():
    return render_template('Exibir.html', Titulo5 = 'Filmes Cadastrados', lista = lista)


@app.route('/contato')
def contato():
    return render_template('Contato.html', Titulo6 = 'Entre em Contato', lista = lista)

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    genero = request.form['genero']
    produtor = request.form['produtor']
    classificacao = request.form['classificacao']
    filme = [nome, genero, produtor,classificacao]
    lista.append(filme)
    return redirect('/exibir')



if __name__ == '__main__':
    app.run()

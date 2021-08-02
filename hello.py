'''
1º [Linha 12] - Importando a classe Flask do módulo flask
2º [Linha 13] - Importando a função render_template
3º [Linha 15] - Criando uma instância de um objeto Flask e atribuindo-o à variável app
4º [Linha 17] - O decorador @route permite associar um caminho web da URL a função Python definida
5º [Linha 18 e 19] - A Função quando é chamada, retorna a mensagem definida na função
6º [Linha 21 e 22] - O decorador @route permite associar um comportamento de redirecionamento
com uma requisição obrigatória (name)
7º [Linha 23 e 24] - Quando a função for chamada, o nome do modelo definido será retornado como String,
juntamente, com argumento para ser repassado palavra-chave do modelo definido.
'''
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

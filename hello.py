'''
1º [Linha 07] - Importando a classe Flask do módulo flask
2º [Linha 09] - Criando uma instância de um objeto Flask e atribuindo-o à variável app
3º [Linha 11] - O decorador @route permite associar um caminho web da URL a função Python definida
4º [Linha 12 até 13] - A Função quando é chamada, retona a mensagem definida na função
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

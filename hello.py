'''
1º [Linha 07] - Importando a classe Flask do módulo flask
2º [Linha 09] - Criando uma instância de um objeto Flask e atribuindo-o à variável app
3º [Linha 11] - O decorador @route permite associar um caminho web da URL a função Python definida
4º [Linha 12 até 17] e [Linha 19 até 25] - A Função quando é chamada, retona a mensagem definida na função
'''
from flask import Flask

app = Flask(__name__)

@app.route("/projects/")
def projects():
    '''
    Comportamento de Redirecionamento - Caso URL esteja com barra no final (e.x.: /projects/) no decorador route(),
    significa que se o usuário acessar sem a barra no final da URL, o Flask redireciona para uma URL Canônico.
    '''
    return "The project page"

@app.route("/about")
def about():
    '''
    URL Única - Caso a URL que esteja definida no decorador route() não apresenta barra final,
    significa que está URL é única, mas, se o usuário acessar com uma barra no final da URL, será produzido o erro 404.
    '''
    return "The about page"

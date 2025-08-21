#pip install flask
from flask import Flask, render_template
#criar o app flask
app = Flask(__name__)

#rota para a pagina inicial - as proximas 3 linhas são um decorator e precisa ser sempre essas linhas seguindas
@app.route('/')
def inicio():
    return "<h1>hello world</h1> <br> <he> Bem vindo a minha página inicial <br> <a href='/contato'>Fale comigo</h3>"

#rota para a pagina de contatos
@app.route('/contato')
def contato(): #na proxima linha se usar " fora uda '' dentro "
    return "<a href='mailto:gabrielcapassi@gmail.com'> me mande um e-mail! <hr> <a href='/'> <<< Voltar </a>" 

#rota com variaveis na url <H1> serve para Titulos ------ http://127.0.0.1:5000/especial/gabriel
@app.route('/especial/<nome>')
def rotaespecial(nome):
    return f"<h1> Seja bem-vindo {nome} ao meu sistema! </h1>"


#toda aplicação para rodar precisa ter:
if __name__ == '__main__':
    app.run(debug=True)
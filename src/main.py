from flask import Flask,render_template, request, redirect
from data.evento import Evento
eventos = [
    Evento(nome="Almoço", local="Restaurante", data="23/02/2023"),
    Evento(nome="Instrução", local="A6/A8", data="23/02/2023"),
]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", nome_desenvolvedor="Murilo Zanini", eventos=eventos)

@app.route("/novo")
def cadastrar_novo():
    return render_template("cadastrar.html")

@app.route('/criar', methods=['POST'])
def criar():
    nome = request. form['nome']
    data = request. form['data']
    local = request. form['local']
    evento = Evento(nome, data, local)
    global eventos
    eventos.append(evento)
    return redirect('/')


app.run(host="0.0.0.0", port=3000)
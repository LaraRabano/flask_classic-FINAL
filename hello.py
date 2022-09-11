from flask import Flask

app = Flask(__name__)


@app.route('/')
def hola():
    return "Hola, soy Flask"


@app.route('/adios')
def otra():
    return "Hasta luego!"

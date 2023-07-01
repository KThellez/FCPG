from flask import Flask, render_template

app = Flask(__name__)

data_home = {
    "titulo_pagina": 'home',
    "titulo_h1": 'Hola Mundo' 
}

@app.route('/')
def index():
    return render_template('index.html', home = data_home)

@app.route('/login')
def login():
    pass

@app.route('/register')
def register():
    pass

@app.route('/Modelo1')
def modelo_uno():
    pass

@app.route('/Modelo2')
def modelo_dos():
    pass

@app.route('/Modelo3')
def modelo_tres():
    pass

if __name__ == '__main__':
    app.run(debug=True, port=7777)
from flask import Flask, render_template, request, url_for, redirect , flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from config import config
from flask_login import LoginManager, login_user, logout_user
from .consts import *

from .models.ModeloNotasGrupo import ModeloNotasGrupo
from .models.ModeloUsuario import ModeloUsuario

from .models.entities.Usuario import Usuario

app = Flask(__name__)

class LoginForm(FlaskForm):
    user = StringField('Usuario', validators=[InputRequired()])
    password = PasswordField('Contraseña', validators=[InputRequired()])

csrf = CSRFProtect(app)
db = MySQL(app)
login_manager_app=LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModeloUsuario.obtener_por_id(db,id)



@app.route('/')
def index():
    print('estamos realizando la petición en index...')
    data = {
    "titulo_pagina": 'home',
    "titulo_h1": 'Hola Mundo' 
    }
    return render_template('index.html', home = data)

usuario_sign_in = None

@app.route('/plataforma')
def plataforma():
    global usuario_sign_in
    print('El valor es')
    print(usuario_sign_in)
    return render_template('plataforma.html', usuario_nombre = usuario_sign_in)

@app.before_request
def before_request():
    print('antes de la petición')


@app.after_request
def after_request(response):
    print('después de la petición')
    return response


@app.route('/temas')
def temas():
    print('estamos realizando la petición en temas...')
    data = {
    "titulo_pagina": 'temas',
    "titulo_h1": 'Los temas que la plataforma propone son:' 
    }
    pronosticos = {
        'Pronóstico SES': ['Simple Exponential Smoothing (SES) es un método de pronóstico que asigna un peso exponencial decreciente a las observaciones pasadas. Es útil para datos con tendencia y sin patrones estacionales.'],
        'Pronóstico Holt': ['Holt es un método de pronóstico que extiende el modelo SES al incorporar un componente de tendencia. Es útil cuando los datos tienen una tendencia lineal.'],
        'Pronóstico Winters': ['El método de pronóstico de Winters es adecuado para datos con tendencia y estacionalidad. Utiliza un modelo aditivo o multiplicativo para pronosticar datos estacionales.'],
        'Pronóstico ARIMA': ['El modelo ARIMA (Autoregressive Integrated Moving Average) es un enfoque ampliamente utilizado para pronósticos de series temporales. Combina componentes autoregresivos, de media móvil y de diferenciación.'],
        'Pronóstico SARIMA': ['El modelo SARIMA (Seasonal ARIMA) es una extensión del modelo ARIMA que también tiene en cuenta la estacionalidad de los datos. Es útil cuando los datos exhiben patrones estacionales.'],
        'Pronóstico ARIMAX': ['El modelo ARIMAX es similar al modelo ARIMA, pero también incluye variables exógenas como predictores. Es útil cuando se dispone de información adicional que puede mejorar el pronóstico.'],
        'Pronóstico Prophet': ['Prophet es una librería de código abierto desarrollada por Facebook para pronósticos de series temporales. Utiliza un modelo aditivo que incluye tendencia, estacionalidad y efectos de días festivos.'],
        'Pronóstico LSTM': ['Las redes neuronales recurrentes de memoria a largo plazo (LSTM) son una arquitectura de aprendizaje profundo que puede ser utilizada para pronósticos de series temporales. Es capaz de capturar relaciones de largo plazo en los datos.'],
        'Pronóstico Random Forest': ['Random Forest es un algoritmo de aprendizaje automático que se puede utilizar para pronósticos. Combina múltiples árboles de decisión para obtener un pronóstico final.']
    }
    valor1 = request.args.get('valor1')
    return render_template('temas.html', temas = data , pronosticos = pronosticos, valor = valor1)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    global usuario_sign_in
    if request.method == "POST":
        usuario = Usuario(None, request.form['user'], request.form['password'], None)
        usuario_logeado = ModeloUsuario.login(db, usuario)
        if usuario_logeado != None:
            usuario_sign_in= usuario.nombre_usuario
            login_user(usuario_logeado)
            return redirect(url_for('plataforma'))
        else:
            usuario_sign_in = None
            flash(LOGIN_CREDENCIALES_INVALIDAS)
            return render_template('auth/login.html', form=form)
    else:
        return render_template('auth/login.html', form=form)
    

@app.route('/logout')
def logout():
    global usuario_sign_in
    usuario_sign_in = None
    logout_user()
    flash(LOGOUT_EXITOSO)
    return redirect(url_for('login'))


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


#Errores!
def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404



#RUTA DE PRUEBA
@app.route('/estudiantes')
def listar_estudiantes():
    estudiantes = {}
    try:
        estudiantes_lista = ModeloNotasGrupo.listar_estudiantes(db, '1', 'Grupo 2 - Docente Uno')
        print("ABAJO LA LISTA QUE LLEGA DE ESTUDIANTE")
        print(estudiantes_lista)
        data={
            'estudiante':estudiantes_lista
        }
        print('ESTO ESTA EN DATA')
        print(data)
        return render_template('listar_estudiantes.html', data=data)
    except Exception as ex:
        print(ex)
    return []



def inicializar_app(config):
    app.config.from_object(config)
    csrf.init_app(app)
    app.register_error_handler(404, pagina_no_encontrada)
    app.add_url_rule('/', view_func=index)
    app.run(port=7777)
    return app
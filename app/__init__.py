from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)


@app.route('/')
def index():
    print('estamos realizando la petición en index...')
    data = {
    "titulo_pagina": 'home',
    "titulo_h1": 'Hola Mundo' 
    }
    return render_template('index.html', home = data)


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
    print(request.method)
    if request.method == 'POST':
        print(request.form['user'])
        print(request.form['password'])
        return 'OK'
    else:
        return render_template('auth/login.html')

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

def inicializar_app(config):
    app.config.from_object(config)
    app.register_error_handler(404, pagina_no_encontrada)
    app.add_url_rule('/', view_func=index)
    app.run( port=7777)
    return app
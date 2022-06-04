#Importamos las librerias
from flask import Flask, redirect, render_template, request, url_for, flash

#Objeto para inicilizar la aplicacion
app = Flask(__name__, template_folder='templates')

#Clave  de la app
app.secret_key = '090700'

#Controlador de la ruta inicial
@app.route('/')
def principal():
    return render_template('principal.html')

#Main de la app
if __name__ == '__main__':
    app.run(debug=True)
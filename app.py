# app.py
from flask import Flask, render_template, request
from iva_calculador import calcular_iva

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None

    if request.method == 'POST':
        opcion = request.form['opcion']
        valor = float(request.form['valor'])

        resultado = calcular_iva(opcion, valor)

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

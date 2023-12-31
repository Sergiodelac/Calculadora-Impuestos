from flask import Flask, render_template, request
from iva_calculador import calcular_iva
from honorarios_calculador import calcular_honorarios
from comisiones_calculador import calcular_comisiones
from desperdicios_calculador import calcular_desperdicios
from fletes_calculador import calcular_fletes
from renta_calculador import calcular_renta

app = Flask(__name__)

@app.route('/')
def index():
    # Esta función manejará la página de inicio
    return render_template('index.html')

@app.route('/calculadora_iva', methods=['GET', 'POST'])
def calculadora_iva():
    resultado = None

    if request.method == 'POST':
        opcion = request.form.get('opcion')
        valor = request.form.get('valor')

        # Validar si 'opcion' y 'valor' tienen valores antes de calcular
        if opcion and valor:
            resultado = calcular_iva(opcion, valor)
        else:
            resultado = "Error: Debes seleccionar una opción y proporcionar un valor."

    return render_template('iva.html', resultado=resultado)

@app.route('/calculadora_honorarios', methods=['GET', 'POST'])
def calculadora_honorarios():
    resultado = None

    if request.method == 'POST':
        opcion = request.form.get('opcion')
        valor = request.form.get('valor')
        resultado = calcular_honorarios(opcion, valor)

    return render_template('honorarios_calculador.html', resultado=resultado)

@app.route('/calculadora_comisiones', methods=['GET', 'POST'])
def calculadora_comisiones():
    resultado = None

    if request.method == 'POST':
        opcion = request.form.get('opcion')
        valor = request.form.get('valor')
        resultado = calcular_comisiones(opcion, valor)

    return render_template('comisiones_calculador.html', resultado=resultado)


@app.route('/calculadora_desperdicios', methods=['GET', 'POST'])
def calculadora_desperdicios():
    resultado = None

    if request.method == 'POST':
        opcion = request.form.get('opcion')
        valor = float(request.form.get('valor'))

        resultado = calcular_desperdicios(opcion, valor)

    return render_template('desperdicios_calculador.html', resultado=resultado)

@app.route('/calculadora_fletes', methods=['GET', 'POST'])
def calculadora_fletes():
    resultado = None
    if request.method == 'POST':
        opcion = request.form.get('opcion')
        valor = float(request.form.get('valor'))

        resultado = calcular_fletes(opcion, valor)

    return render_template('fletes_calculador.html', resultado=resultado)
    
@app.route('/calculadora_renta', methods=['GET', 'POST'])
def calculadora_renta():
    if request.method == 'POST':
        opcion = request.form['opcion']
        valor = float(request.form['valor'])
        resultado = calcular_renta(opcion, valor)
        return render_template('renta_calculador.html', resultado=resultado)
    return render_template('renta_calculador.html')

@app.route('/tutorial')
def tutorial():
 return render_template('tutorial.html')


if __name__ == '__main__':
    app.run(debug=True)


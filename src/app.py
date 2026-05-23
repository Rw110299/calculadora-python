from flask import Flask, render_template, request
from calculadora import somar, subtrair, multiplicar, dividir

app = Flask(__name__,
            template_folder='../templates',
            static_folder='../static')


@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None

    if request.method == 'POST':
        numero1 = float(request.form['numero1'])
        numero2 = float(request.form['numero2'])
        operacao = request.form['operacao']

        try:
            if operacao == '+':
                resultado = somar(numero1, numero2)

            elif operacao == '-':
                resultado = subtrair(numero1, numero2)

            elif operacao == '*':
                resultado = multiplicar(numero1, numero2)

            elif operacao == '/':
                resultado = dividir(numero1, numero2)

        except Exception as erro:
            resultado = f'Erro: {erro}'

    return render_template('index.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True)
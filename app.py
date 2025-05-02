from flask import Flask, render_template, request
from predictor import predecir_enfermedad

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    sintomas_seleccionados = None

    if request.method == 'POST':
        s1 = int(request.form['sintoma1'])
        s2 = int(request.form['sintoma2'])
        s3 = int(request.form['sintoma3'])

        resultado, sintomas_seleccionados = predecir_enfermedad(s1, s2, s3)

    return render_template('index.html', resultado=resultado, sintomas=sintomas_seleccionados)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

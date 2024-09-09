from flask import Flask, render_template, request
from src.mapa import gerar_mapa

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    cidade_inicio = 'rio_do_sul'
    cidade_fim = 'rio_do_sul'

    if request.method == 'POST':
        cidade_inicio = request.form.get('cidade_inicio')
        cidade_fim = request.form.get('cidade_fim')

    mapa = gerar_mapa(cidade_inicio, cidade_fim)
    return render_template('index.html', mapa=mapa)

if __name__ == '__main__':
    app.run(debug=True)

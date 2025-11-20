from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template(template_name_or_list='home.html')


@app.route('/consulta_saldo')
def consulta_saldo():
    return render_template(template_name_or_list='consultaSaldo.html')

@app.route('/movimentar')
def movimentar():
    return render_template(template_name_or_list='tipo_de_movimentacao.html')

@app.route('/cadastro')
def cadastro():
    return render_template(template_name_or_list='cadastro.html')

@app.route('/saldo')
def saldo():
    return render_template(template_name_or_list='saldo.html')

@app.route('/depositar')
def depositar():
    return render_template(template_name_or_list='depositar.html')

@app.route('/sacar')
def sacar():
    return render_template(template_name_or_list='sacar.html')


if __name__ == "__main__":
    app.run(debug=True)

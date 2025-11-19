from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template(template_name_or_list='home.html')

@app.route('/consulta_saldo')
def movimentar():
    return render_template(template_name_or_list='consultaSaldo.html')
@app.route('/movimentar')
def consulta_saldo():
    return render_template(template_name_or_list='movimentacao.html')
@app.route('/cadastro')
def cadastro():
    return render_template(template_name_or_list='cadastro.html')

if __name__ == "__main__":
    app.run(debug=True)

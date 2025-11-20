from flask import Flask, render_template, request, redirect, session, flash, url_for

from src.backend.Cliente import Cliente

app = Flask(__name__)

clientes = []

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

@app.route('/cadastrar_cliente', methods=['POST'])
def cadastrar_cliente():
    nome = request.form['nome']
    cpf = request.form['cpf']
    tempCliente = Cliente(nome, cpf)
    clientes.append(tempCliente)
    for cliente in clientes:
        print(cliente.nome)
        print(cliente.cpf)
        
    return redirect(url_for('criarConta'))
@app.route('/criarConta')
def criarConta():
    return render_template(template_name_or_list='criarConta.html')
@app.route('/escolherconta', methods=['POST'])
    return render_template(template_name_or_list='main.html')
    

if __name__ == "__main__":
    app.run(debug=True)

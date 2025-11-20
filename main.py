from flask import Flask, render_template, request, redirect, session, flash, url_for

from src.backend.Cliente import Cliente
from src.backend.Conta_corrente import ContaCorrente
from src.backend.Conta_poupanca import ContaPoupanca
from src.backend.Conta_salario import ContaSalario 

app = Flask(__name__)

clientes = [Cliente("Fulano de Tal", "12345678900"),
                Cliente("Ciclano da Silva", "98765482100"),
                Cliente("Beltrano Souza", "45678912300"),
                Cliente("Maria Oliveira", "32165498700")]

contas = [ContaCorrente(clientes[0]),
              ContaPoupanca(clientes[1]),
              ContaSalario(clientes[2]),
              ContaCorrente(clientes[3])]

@app.route('/')
def main():
    return render_template(template_name_or_list='home.html')



@app.route('/movimentar')
def movimentar():
    return render_template(template_name_or_list='tipo_de_movimentacao.html')

@app.route('/cadastro')
def cadastro():
    return render_template(template_name_or_list='cadastro.html')

# ...existing code...
@app.route('/saldo', methods=['GET', 'POST'])
def saldo():
    cpf = None
    if request.method == 'POST':
        cpf = request.form.get('cpf')
    return render_template(template_name_or_list='saldo.html', contas=contas, cpf=cpf)
# ...existing code...

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
#Teste
    for cliente in clientes:
        print(cliente.nome)
        print(cliente.cpf)
    return redirect(url_for('criarConta'))

@app.route('/criarConta')
def criarConta():
    return render_template(template_name_or_list='criarConta.html')

@app.route('/escolherConta', methods=['POST',])
def escolherConta():
    tipo = request.form['tipo']
    match tipo:
        case 'corrente':
            nova_conta = ContaCorrente(clientes[-1])
        case 'poupanca':
            nova_conta = ContaPoupanca(clientes[-1])
        case 'salario':
            nova_conta = ContaSalario(clientes[-1])
#Teste
    contas.append(nova_conta)
    for conta in contas:
        print(conta.numero)
        print(conta.titular.nome)
        print(type(conta))
    return render_template(template_name_or_list='home.html')

@app.route('/exibirTudo')
def exibirTudo():
    return render_template(template_name_or_list='exibirTudo.html', contas=contas)

    

if __name__ == "__main__":
    app.run(debug=True)

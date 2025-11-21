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

@app.route('/saldo', methods=['GET', 'POST'])
def saldo():
    conteudo_html = ""
    if request.method == 'POST':
        cpf = request.form.get('cpf')
        if cpf:
            for conta in contas:
                if conta.titular.cpf == cpf:
                    conteudo_html = f'<p>O saldo da conta numero { conta.numero } do titular {conta.titular.nome} é: { conta.saldo }</p>'
                    return render_template(template_name_or_list='saldo.html', conteudo=conteudo_html)
            conteudo_html = '<p>CPF informado Inválido! Verifique o CPF informado e tente novamente.</p>'
            return render_template(template_name_or_list='saldo.html', conteudo=conteudo_html)
    return render_template(template_name_or_list='saldo.html', conteudo=conteudo_html)

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
    contas.append(nova_conta)
    conteudo_html = f'<p>Conta {tipo} criada com sucesso para o cliente {clientes[-1].nome} do CPF {clientes[-1].cpf}!</p><p>Número da conta: {nova_conta.numero}</p><p>Saldo inicial: {nova_conta.saldo}</p>'
    return render_template(template_name_or_list='home.html', conteudo=conteudo_html)

@app.route('/exibirTudo')
def exibirTudo():
    return render_template(template_name_or_list='exibirTudo.html', contas=contas)

@app.route('/deposito', methods=['POST'])
def deposito():
    conteudo_html = ""
    cpf = request.form['cpf']
    valor = float(request.form['valor'])
    for conta in contas:
        if conta.titular.cpf == cpf:
            conta.depositar(valor)
            conteudo_html = f'<p>Depósito de {valor} realizado com sucesso na conta {conta.numero} do titular {conta.titular.nome}!</p><p> Saldo atual: {conta.saldo}</p>'
            return render_template(template_name_or_list='depositar.html',conteudo = conteudo_html)
    conteudo_html = '<p>CPF informado Inválido! Verifique o CPF informado e tente novamente.</p>'
    return render_template(template_name_or_list='depositar.html',conteudo = conteudo_html)

@app.route('/saque', methods=['POST'])
def saque():
    conteudo_html = ""
    cpf = request.form['cpf']
    valor = float(request.form['valor'])
    for conta in contas:
        if conta.titular.cpf == cpf:
            retornado = conta.sacar(valor)
            if retornado is None:
                conteudo_html = f'<p>Saldo insuficiente para saque de {valor} na conta {conta.numero} do titular {conta.titular.nome}!</p><p> Saldo atual: {conta.saldo}</p>'
                return render_template(template_name_or_list='sacar.html',conteudo = conteudo_html)
            conteudo_html = f'<p>Depósito de {valor} realizado com sucesso na conta {conta.numero} do titular {conta.titular.nome}!</p><p> Saldo atual: {conta.saldo}</p>'
            return render_template(template_name_or_list='sacar.html',conteudo = conteudo_html)
    conteudo_html = '<p>CPF informado Inválido! Verifique o CPF informado e tente novamente.</p>'
    return render_template(template_name_or_list='sacar.html',conteudo = conteudo_html)


if __name__ == "__main__":
    app.run(debug=True)

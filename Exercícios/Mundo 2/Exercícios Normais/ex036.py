print('==== Empréstimo Bancário ====')
VdaCasa = float(input('Qual o valor da casa que você deseja comprar? R$'))
Sal = float(input('Qual o seu salário? R$'))
Apagar = int(input('Em quantos anos você pretende pagar a casa? '))
if VdaCasa / (Apagar * 12) <= Sal * 30 / 100:
    print('O seu emprestimo foi ACEITO!!')
else:
    print('Desculpe, o empréstimo foi NEGADO!')

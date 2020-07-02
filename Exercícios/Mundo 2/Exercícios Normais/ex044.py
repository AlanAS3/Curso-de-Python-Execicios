print('==== Gerenciador de pagamentos ====')
Vpro = float(input('Digite o valor do produto R$'))
cond = int(input("""=== Formas de pagamento ===
[1] à vista (dinheiro/cheque) - 10% de desconto
[2] à vista no cartão - 5% de desconto
[3] em até 2x no cartão - preço normal
[4] 3x ou mais no cartão - 20% de juros
-- Qual a forma de pagamento []: """))
if cond == 1:
    Vpro = Vpro - (10/100 * Vpro)
    print(f'O seu produto vai sair por {Vpro:.2f} à vista')
elif cond == 2:
    Vpro = Vpro - (5/100 * Vpro)
    print(f'O seu produto vai sair por {Vpro:.2f} à vista no cartão')
elif cond == 3:
    print(f'O seu produto vai sair por {Vpro:.2f} em até 2x no cartão')
elif cond == 4:
    Vpro = Vpro + (20/100 * Vpro)
    print(f'O seu produto vai sair por {Vpro:.2f} em 3x ou mais no cartão')

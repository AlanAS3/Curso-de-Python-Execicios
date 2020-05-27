print('==== Calculo de descontos (5%) ====')
prod = float(input('Digte o preço do produto R$'))
Npre = float(prod - ((5/100)*prod))
print(f'Com 5% de desconto o produto fica R${Npre:.2f}')

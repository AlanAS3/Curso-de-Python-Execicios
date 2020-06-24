print('\033[32;1m==== Calculo de descontos (5%) ====\033[m')
prod = float(input('\033[31mDigte o preço do produto R$'))
Npre = float(prod - ((5/100)*prod))
print(f'\033[36;1mCom 5% de desconto o produto fica R$\033[34;1m{Npre:.2f}')

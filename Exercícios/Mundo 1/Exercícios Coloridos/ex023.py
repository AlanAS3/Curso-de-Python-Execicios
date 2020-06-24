print('\033[32;1m=== Separando dígitos de um número ===\033[m')
num = int(input('\033[31mDigite um número entre 0 e 9999: \033[m'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'\033[36mUnidade: \033[34;1m{u}\033[m\n\033[36mDezena: \033[34;1m{d}\033[m')
print(f'\033[36mCentena: \033[34;1m{c}\033[m\n\033[36mMilhar: \033[34;1m{m}\033[m')

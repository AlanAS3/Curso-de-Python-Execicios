print('\033[32;1m=== Custo de Viagem ===\033[m')
km = float(input('\033[31mQual a distância da sua viagem em Km: '))
if km <= 200:
    valor = km * 0.50
    print(f'\033[36mA sua viagem vai custar: R$\033[34;1m{valor}\033[m')
else:
    valor = km * 0.45
    print(f'\033[36mQue local distante, a sua viagem vai custar: R$\033[34;1m{valor}\033[m')

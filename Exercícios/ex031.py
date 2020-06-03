print('=== Custo de Viagem ===')
km = float(input('Qual a distância da sua viagem em Km: '))
if km < 200:
    valor = km * 0.50
    print(f'A sua viagem vai custar: R${valor}')
else:
    valor = km * 0.45
    print(f'Que local distante, a sua viagem vai custar: R${valor}')

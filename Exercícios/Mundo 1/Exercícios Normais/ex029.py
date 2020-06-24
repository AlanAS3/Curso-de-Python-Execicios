print('=== Radar Eletrônico ===')
Vel = float(input('Qual a velocidade do seu carro? '))
if Vel > 80.0:
    multa = (Vel - 80.0) * 7
    print(f'Você está acima da velocidade, a sua multa é de {multa}')
    print('A velocidade permitida é de 80Km/h')
else:
    print('Você está dentro da velocidade permitida, continue assim')

print('\033[32;1m=== Radar Eletrônico ===\033[m')
Vel = float(input('\033[31mQual a velocidade do seu carro? '))
if Vel > 80.0:
    multa = (Vel - 80.0) * 7
    print(f'\033[36mVocê está acima da velocidade, a sua multa é de \033[34;1m{multa}\033[m')
    print('\033[36mA velocidade permitida é de 80Km/h')
else:
    print('\033[36mVocê está dentro da velocidade permitida, continue assim')

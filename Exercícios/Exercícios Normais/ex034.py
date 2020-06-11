print('=== Aumento de Salário ===')
Sal = float(input('Qual o seu salário? '))
if Sal >= 1250.00:
    Sal = Sal + Sal * (10 / 100)
    print(f'O seu novo salário é de {Sal}')
else:
    Sal = Sal + Sal * (15 / 100)
    print(f'O seu novo salário é de {Sal}')

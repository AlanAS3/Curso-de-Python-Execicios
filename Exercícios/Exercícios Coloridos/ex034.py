print('\033[32;1m=== Aumento de Salário ===\033[m')
Sal = float(input('\033[31mQual o seu salário? '))
if Sal >= 1250.00:
    Sal = Sal + Sal * (10 / 100)
    print(f'\033[36mO seu novo salário é de \033[34;1m{Sal}\033[m')
else:
    Sal = Sal + Sal * (15 / 100)
    print(f'\033[36mO seu novo salário é de \033[34;1m{Sal}\033[m')

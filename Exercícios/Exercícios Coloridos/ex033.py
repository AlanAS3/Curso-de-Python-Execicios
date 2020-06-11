print('\033[32;1m=== Mairo e Menor Número ===\033[m')
n1 = int(input('\033[31mDigite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n1 > n2 and n1 > n3:
    print(f'\033[34;1m{n1}\033[m\033[36m é o maior número')
else:
    if n2 > n1 and n2 > n3:
        print(f'\033[34;1m{n2}\033[m\033[36m é o maior número')
    else:
        print(f'\033[34;1m{n3}\033[m\033[36m é o maior número')
if n1 < n2 and n1 < n3:
    print(f'\033[34;1m{n1}\033[m\033[36m é o menor número')
else:
    if n2 < n1 and n2 < n3:
        print(f'\033[34;1m{n2}\033[m\033[36m é o menor número')
    else:
        print(f'\033[34;1m{n3}\033[m\033[36m é o menor número')

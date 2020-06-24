print('==== Comparando números ====')
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print(f'O PRIMEIRO valor ({n1}) é maior')
elif n2 > n1:
    print(f'O SEGUNDO valor ({n2}) é maior')
else:
    print('Não existe valor maior, os dois são iguais')

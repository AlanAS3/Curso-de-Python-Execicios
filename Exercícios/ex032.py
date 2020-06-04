print('=== Ano Bissexto ===')
ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 400 == 0:
    print('Esse é um ano BISSEXTO')
else:
    print('Esse NÃO é um ano Bissexto')

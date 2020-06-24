print('\033[32;1m=== Ano Bissexto ===\033[m')
ano = int(input('\033[31mDigite um ano: '))
if ano % 4 == 0 and ano % 400 == 0:
    print('\033[36;1mEsse é um ano BISSEXTO')
else:
    print('\033[36;1mEsse NÃO é um ano Bissexto')

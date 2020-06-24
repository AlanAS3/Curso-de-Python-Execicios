print('===== Analisando Triângulos V2.0 =====')
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Essas retas PODEM formar um triângulo!')
    if r1 == r2 and r2 == r3:
        print('O triângulo é do tipo: EQUILÁTERO ')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('O triângulo é do tipo: ISÓSCELES')
    else:
        print('O triângulo é do tipo: ESCALENO')
else:
    print('Essas retas NÂO PODEM formar um triângulo!')
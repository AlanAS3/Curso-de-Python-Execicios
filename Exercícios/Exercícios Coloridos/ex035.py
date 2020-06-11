print('\033[32;1m=== Analisando Triângulo ===\033[m')
r1 = float(input('\033[31mDigite o comprimento da primenra reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1+r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('\033[36;1mEssas retas PODEM foramr um triângulo')
else:
    print('\033[36;1mEssas retas NÃO podem formar um triângulo')

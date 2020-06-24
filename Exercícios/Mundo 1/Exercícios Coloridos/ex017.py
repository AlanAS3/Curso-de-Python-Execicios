from math import hypot
print('\033[32;1m==== Catetos e Hipotenusa ====\033[m')
catOposto = float(input('\033[31mDigite o comprimento do cateto oposto: '))
catAdjace = float(input('Digte o comprimento do cateto adjacente: '))
hipo = hypot(catOposto, catAdjace)
print(f'\033[36mA hipotenusa desse triângulo retângulo é \033[34;1m{hipo:.1f}')

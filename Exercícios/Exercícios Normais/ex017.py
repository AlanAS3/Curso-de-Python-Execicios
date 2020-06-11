from math import hypot
print('==== Catetos e Hipotenusa ====')
catOposto = float(input('Digite o comprimento do cateto oposto: '))
catAdjace = float(input('Digte o comprimento do cateto adjacente: '))
hipo = hypot(catOposto, catAdjace)
print(f'A hipotenusa desse triângulo retângulo é {hipo:.1f}')

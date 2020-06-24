import math
print('\033[32;1m==== Seno, Cosseno e Tangente ====\033[m')
angulo = math.radians(int(input('\033[31mDigte o valor de um ângulo qualquer: ')))
print(f'\033[36mPara o ângulo de \033[34;1m{math.degrees(angulo):.1f}°\033[m\033[36m, o seno é \033[34;1m{math.sin(angulo):.2f}\033[m\033[36m, cosseno \033[34;1m{math.cos(angulo):.2f}\033[m\033[36m e a tangente \033[34;1m{math.tan(angulo):.2f}.')

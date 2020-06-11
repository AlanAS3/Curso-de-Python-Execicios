print('\033[32;1m==== Quebrando um número ====\033[m')
from math import trunc
num = float(input('\033[31mDigite um número real: '))
print(f'\033[36mO número \033[34;1m{num} \033[36mtem a parte inteira sendo \033[34;1m{trunc(num)}')

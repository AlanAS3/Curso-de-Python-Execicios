import random
print('\033[32;1m==== Ordem de apresentção dos alunos ====\033[m')
A1 = input('\033[31mDigite o nome do primeiro aluno: ')
A2 = input('Digite o nome do segundo aluno: ')
A3 = input('Digite o nome do terceiro aluno: ')
A4 = input('Digite o nome do quarto aluno: ')
seq = (A1,A2,A3,A4)
print(f'\033[36mA oredem da apresentação é:\n\033[32;1m{random.sample(seq, k=4)}')

import random
print('==== Ordem de apresentção dos alunos ====')
A1 = input('Digite o nome do primeiro aluno: ')
A2 = input('Digite o nome do segundo aluno: ')
A3 = input('Digite o nome do terceiro aluno: ')
A4 = input('Digite o nome do quarto aluno: ')
seq = (A1,A2,A3,A4)
print(f'A oredem da apresentação é:\n{random.sample(seq, k=4)}')

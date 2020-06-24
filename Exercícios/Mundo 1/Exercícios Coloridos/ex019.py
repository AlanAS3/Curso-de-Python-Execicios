from random import choice
print('\033[32;1m==== Sorteio de aluno ====\033[m')
A1 = input('\033[31mDigite o nome do primeiro aluno: ')
A2 = input("Digite o nome do segundo aluno: ")
A3 = input('Digite o nome do terceiro aluno: ')
A4 = input('Digite o nome do quarto aluno: ')
seq = (A1, A2, A3, A4)
print(f'\033[36mO aluno sorteado para apagar a quadro é \033[34;1m{choice(seq)}')

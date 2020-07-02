from random import choice
from time import sleep
print('==== Pedra, Papel e Tesoura ====')
print('-=' * 35)
print('Vamos brincar de Jokenpô, vamos ver se você consegue me vencer :)')
print('-=' * 35)
j = str(input('-> O que você escolhe (Pedra, Papel ou Tesoura)? ')).upper().strip()
l = ('PEDRA', 'PAPEL', 'TESOURA')
comp = choice(l)
print('Processando...')
sleep(1)
if j == 'PEDRA' and comp == 'TESOURA' or j == 'TESOURA' and comp == 'PAPEL' or j == 'PAPEL' and comp == 'PEDRA':
    print(f'Você venceu, parabêns!! Eu joguei {comp}')
elif j == comp:
    print(f'Parece que foi empate, porque eu jogeui {comp} também, que coisa em :/')
elif comp == 'PEDRA' and j == 'TESOURA' or comp == 'TESOURA' and j == 'PAPEL' or comp == 'PAPEL' and j == 'PEDRA':
    print(f'Eu venci! Eu joguei {comp}. Foi bom jogar com você :)')
else:
    print('ERRO. Por favor tente novamente')

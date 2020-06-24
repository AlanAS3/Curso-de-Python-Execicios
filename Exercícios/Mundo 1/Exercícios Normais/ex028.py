from random import randint
print('=== Jogo da adivinhação ===')
n = int(input('Adivinhe o número entre 0 e 5 que eu estou pensando: '))
r = randint(0,5)
if n == r:
    print('Sortudo, você acertou o número que eu estava pensando, PARABÉNS!')
else:
    print(f'Sinto muito, você errou, o número que eu tava pensando era {r}')

from random import randint
print('\033[32;1m=== Jogo da adivinhação ===\033[m')
n = int(input('\033[31mAdivinhe o número entre 0 e 5 que eu estou pensando: '))
r = randint(0,5)
if n == r:
    print('\033[36mSortudo, você acertou o número que eu estava pensando, PARABÉNS!')
else:
    print(f'\033[36mSinto muito, você errou, o número que eu tava pensando era \033[34;1m{r}')

import pygame
print('\033[32;1m==== Ouvindo Música ====\033[m')
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
while (pygame.mixer.music.get_busy()):pass

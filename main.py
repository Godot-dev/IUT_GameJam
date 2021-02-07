import pygame
from pygame.constants import MOUSEBUTTONDOWN
from classes.game import Game
from classes.menu import Menu
from classes.options import Options

# Instanciations obligatoires initiales
pygame.init()
pygame.display.set_caption("Game")
screen = pygame.display.set_mode((1024, 768))
game = Game()
menu = Menu()
options = Options()
running = True
background = pygame.image.load('assets/background.png')



while running: 
    screen.blit(background, (0, 0))

    if game.is_playing: # Si on est en jeu, on lance la boucle du jeu
        game.boucleJeu(screen)
    elif options.is_configure: 
        options.drawOptions(screen)
    else: 
        menu.drawMenu(screen)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN and not game.is_playing:
            if not menu.catch_signal(game,options,event): # Si la fonction renvoit faux, on doit arrêter le programme
                running = False
                pygame.quit()


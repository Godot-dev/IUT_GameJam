import pygame
from pygame.constants import MOUSEBUTTONDOWN
from classes.game import Game
from classes.menu import Menu
from classes.options import Options

# Instanciations obligatoires initiales
pygame.init()
pygame.display.set_caption("Game")
screen = pygame.display.set_mode((1024, 768)) # Taille fixe du jeu, imposée dans les consignes, ne pas changer
game = Game()
menu = Menu()
options = Options()
running = True

while running: 
    if game.is_playing: # Si on est en jeu, on lance la boucle du jeu
        game.drawJeu(screen)
    elif options.is_configure: # Si on est dans les options, on affiche les options
        options.drawOptions(screen)
    else: # Sinon on affiche le menu principal (c'est ce qui se passe quand on lance le jeu)
        menu.drawMenu(screen)

    pygame.display.flip() # On mets à jour l'écran à chaque itération de la boucle

    for event in pygame.event.get(): # Pour tous les events de l'itération de boucle en question
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif game.is_playing:
            game.catch_signal(event)
        elif event.type == MOUSEBUTTONDOWN and options.is_configure:
            options.catch_signal(event)
        elif event.type == MOUSEBUTTONDOWN and not menu.catch_signal(game,options,event): # Si la fonction renvoit faux, on doit arrêter le programme
                running = False
                pygame.quit()
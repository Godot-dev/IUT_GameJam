import pygame
from pygame.constants import MOUSEBUTTONDOWN
from classes.game import Game
from classes.menu import Menu
from classes.credits import Credits

# Instanciations obligatoires initiales
pygame.init()
pygame.display.set_caption("Farmer in deep doo-doo")
screen = pygame.display.set_mode((1024, 768))
game = Game()
menu = Menu()
credits = Credits()
currentEvent = None
running = True
clock = pygame.time.Clock()
music = False

while running: 
    clock.tick(60) 
    if game.is_playing: # Si on est en jeu, on lance la boucle du jeu
        game.drawJeu(screen, pygame.display)
        game.catch_signal(currentEvent)
        currentEvent = None
        game.pressed["Clic"] = False
    elif credits.is_credits: # Si on est dans les options, on affiche les options
        credits.drawCredits(screen)
    else: # Sinon on affiche le menu principal (c'est ce qui se passe quand on lance le jeu)
        if music == False:
            music = True
            pygame.mixer.music.load("assets/music/themeHome/Rio_Bravo_Home.ogg")
            pygame.mixer.music.play()
        menu.drawMenu(screen)
        if(game.perdu == True or game.victoire == True):
            game = Game() # On remets la partie à 0
            music = False # On remets la musique du menu

    pygame.display.flip() # On met à jour l'écran à chaque itération de la boucle

    for event in pygame.event.get(): # Pour tous les events de l'itération de boucle en question
        if event.type == pygame.QUIT:
            running = False

        if game.is_playing:
            # On met à jour pressed
            if event.type == MOUSEBUTTONDOWN:
                game.pressed["Clic"] = True
                currentEvent = event
            else:
                if event.type == pygame.KEYDOWN:
                    game.pressed[event.key] = True
                elif event.type == pygame.KEYUP:
                    game.pressed[event.key] = False
                elif event.type == pygame.K_SPACE:
                    game.pressed[event.key] = False
                elif event.type == pygame.K_RETURN:
                    game.pressed[event.key] = False
        elif event.type == MOUSEBUTTONDOWN and credits.is_credits:
            credits.catch_signal(event)
        elif event.type == MOUSEBUTTONDOWN and not menu.catch_signal(game, credits, event): # Si la fonction renvoie faux, on doit arrêter le programme
            running = False 

        
pygame.quit()
import pygame
from classes.button import Button

class Menu:
    def __init__(self):
        # Instanciation des éléments liés au menu
        self.playButton =    Button(400, 107, 312, 100, 'assets/play.png')
        self.optionsButton = Button(400, 107, 312, 300, 'assets/options.png')
        self.quitButton =    Button(400, 107, 312, 500, 'assets/quit.png')

    def drawMenu(self,screen): # On affiche le menu, chaque bouton est positionné au rectangle formé par sa hitbox
        screen.blit(self.playButton.img, self.playButton.hitbox)
        screen.blit(self.optionsButton.img, self.optionsButton.hitbox)
        screen.blit(self.quitButton.img, self.quitButton.hitbox)

    def catch_signal(self, game, options, event): # Effectue l'action appropriée si l'utilisateur a cliqué sur un des boutons du menu
        if self.playButton.hitbox.collidepoint(event.pos):
            game.is_playing = True
        elif self.optionsButton.hitbox.collidepoint(event.pos):
            options.is_configure = True
        elif self.quitButton.hitbox.collidepoint(event.pos):
            return False # Renvoie False si le programme doit s'arrêter, suite à un appui sur le bouton QUIT
        return True

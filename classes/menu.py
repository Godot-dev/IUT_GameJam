import pygame
from classes.button import Button

class Menu:
    def __init__(self):
        # Instanciation des éléments liés au menu
        self.background = pygame.image.load('assets/Menu/bg.png')
        self.playButton =    Button(260, 107, 382, 300, 'assets/Menu/Jouer.png')
        self.creditsButton = Button(260, 107, 382, 425, 'assets/Menu/Credits.png')
        self.quitButton =    Button(260, 107, 382, 550, 'assets/Menu/quitter.png')
        self.HighScore =    Button(180, 62, 820, 680, 'assets/Menu/HighScore.png')
        self.SandBox =    Button(180, 62, 25, 680, 'assets/Menu/SandBox.png')

    def drawMenu(self,screen): # On affiche le menu, chaque bouton est positionné au rectangle formé par sa hitbox
        screen.blit(self.background, (0, 0))
        screen.blit(self.playButton.img, self.playButton.hitbox)  
        screen.blit(self.creditsButton.img, self.creditsButton.hitbox)
        screen.blit(self.quitButton.img, self.quitButton.hitbox)
        screen.blit(self.HighScore.img, self.HighScore.hitbox)
        screen.blit(self.SandBox.img, self.SandBox.hitbox)
        

    def catch_signal(self, game, credits, event): # Effectue l'action appropriée si l'utilisateur a cliqué sur un des boutons du menu
        if self.playButton.hitbox.collidepoint(event.pos):
            game.is_playing = True
        elif self.creditsButton.hitbox.collidepoint(event.pos):
            credits.is_credits = True
        elif self.quitButton.hitbox.collidepoint(event.pos):
            return False # Renvoie False si le programme doit s'arrêter, suite à un appui sur le bouton QUIT
        return True

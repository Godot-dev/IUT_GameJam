import pygame

class Game:
    def __init__(self):
        # Image de background
        self.background = pygame.image.load('assets/1.png')
        self.is_playing = False


    def drawJeu(self,screen):
        screen.blit(self.background, (0, 0))

    def catch_signal(self,event):
        pass
import pygame

class Options:
    def __init__(self):
        # Image de background
        self.background = pygame.image.load('assets/background.png')
        # Instanciation des éléments liés au menu des options
        self.is_configure = False

    def drawOptions(self,screen):
        screen.blit(self.background, (0, 0))

    def catch_signal(self,event):
        pass

import pygame

class Credits:
    def __init__(self):
        # Image de background
        self.background = pygame.image.load('assets/Crédit.png')
        # Instanciation des éléments liés au menu des options
        self.is_credits = False

    def drawCredits(self,screen):
        screen.blit(self.background, (0, 0))
        

    def catch_signal(self,event):
        pass

import pygame

class Menu:
    def __init__(self):
        # Instanciations des éléments liés au menu
        self.play_button = pygame.image.load('assets/play.png')
        self.play_button = pygame.transform.scale(self.play_button,(400,107)) # On redimensionne
        self.play_button_rect = self.play_button.get_rect() # On implémente la hitbox du bouton
        self.play_button_rect.x = 312
        self.play_button_rect.y = 100
        self.options_button = pygame.image.load('assets/options.png')
        self.options_button = pygame.transform.scale(self.options_button,(400,107)) # On redimensionne
        self.options_button_rect = self.options_button.get_rect() # On implémente la hitbox du bouton
        self.options_button_rect.x = 312
        self.options_button_rect.y = 300
        self.quit_button = pygame.image.load('assets/quit.png') 
        self.quit_button = pygame.transform.scale(self.quit_button,(400,107)) # On redimensionne
        self.quit_button_rect = self.quit_button.get_rect() # On implémente la hitbox du bouton
        self.quit_button_rect.x = 312
        self.quit_button_rect.y = 500


    def drawMenu(self,screen): # on affiche le menu, chaque bouton est positionné au rectangle formé par sa hitbox
        screen.blit(self.play_button,self.play_button_rect)
        screen.blit(self.options_button,self.options_button_rect)
        screen.blit(self.quit_button,self.quit_button_rect)

    def catch_signal(self,game,options,event): # Effectue l'action appropriée si l'utilisateur a cliqué sur un des boutons du menu
        if self.play_button_rect.collidepoint(event.pos):
            game.is_playing = True
        elif self.options_button_rect.collidepoint(event.pos):
            options.is_configure = True
        elif self.quit_button_rect.collidepoint(event.pos):
            return False # Renvoit False si le programme doit s'arrêter, suite a un appui sur le bouton QUIT
        return True
import pygame
from classes.player import Player

class Cauchemar:
    def __init__(self, difficulty, legumes):
        self.player = Player()    
        self.difficulty = difficulty
        self.legumes = legumes

    def drawCauchemar(self, screen):
        screen.blit(self.player.image, self.player.rect)

    def catch_signal(self, pressed):
        print(pressed)
        if pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < 1024:
            self.player.move_right()
        if pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        if pressed.get(pygame.K_UP) and self.player.rect.y > 0:
            self.player.move_up()
        if pressed.get(pygame.K_DOWN) and self.player.rect.y + self.player.rect.height < 768:
            self.player.move_down()

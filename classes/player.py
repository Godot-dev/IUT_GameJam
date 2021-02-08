import pygame

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 3
        self.velocity = 5
        self.image = pygame.image.load('assets/player.png')
        self.image = pygame.transform.scale(self.image,(64,64))
        self.rect = self.image.get_rect()
        self.rect.x = 540
        self.rect.y = 360
        self.imageVie = pygame.image.load('assets/3coeurs.png')

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity
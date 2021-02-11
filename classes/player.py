import pygame

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 3
        self.velocity = 5
        self.image = pygame.image.load('assets/character/character1.png')
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
    
    def dash(self,pressed): # Interdit de dash en diagonale
        for i in range(25):
            if pressed.get(pygame.K_RIGHT) and self.rect.x + self.rect.width < 1024:
                self.rect.x += self.velocity
            elif pressed.get(pygame.K_LEFT) and self.rect.x > 0:
                self.rect.x -= self.velocity
            elif pressed.get(pygame.K_UP) and self.rect.y > 0:
                self.rect.y -= self.velocity
            elif pressed.get(pygame.K_DOWN) and self.rect.y + self.rect.height < 768:
                self.rect.y += self.velocity
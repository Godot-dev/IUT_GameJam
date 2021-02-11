import pygame

pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 3
        self.velocity = 5
        self.imageFront = pygame.image.load('assets/character/charFront.png')
        self.imageFront = pygame.transform.scale(self.imageFront,(64,64))
        self.imageSideRight = pygame.image.load('assets/character/charSideRight.png')
        self.imageSideRight = pygame.transform.scale(self.imageSideRight,(64,64))
        self.imageSideLeft = pygame.image.load('assets/character/charSideLeft.png')
        self.imageSideLeft = pygame.transform.scale(self.imageSideLeft,(64,64))
        self.imageBack = pygame.image.load('assets/character/charBack.png')
        self.imageBack = pygame.transform.scale(self.imageBack,(64,64))
        self.image = self.imageFront
        self.rect = self.image.get_rect()
        self.rect.x = 540
        self.rect.y = 360
        self.imageVie = pygame.image.load('assets/character/3coeurs.png')

    def move_right(self):
        self.image = self.imageSideRight
        self.rect.x += self.velocity

    def move_left(self):
        self.image = self.imageSideLeft
        self.rect.x -= self.velocity

    def move_up(self):
        self.image = self.imageBack
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
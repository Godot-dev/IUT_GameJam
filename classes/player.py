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
        #self.imageVie = pygame.transform.scale(self.imageVie,(128,128))

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity
    
    def dash(self,pressed):
        f = self.velocity
        # Si le joueur va en diagonale, sa vitesse doit être réduite car il va faire deux déplacements en une seule action
        for i in range(20):
            if (pressed.get(pygame.K_RIGHT) and pressed.get(pygame.K_UP)) or (pressed.get(pygame.K_RIGHT) and pressed.get(pygame.K_DOWN)) or (pressed.get(pygame.K_LEFT) and pressed.get(pygame.K_UP)) or (pressed.get(pygame.K_LEFT) and pressed.get(pygame.K_DOWN)):
                f *= 0.7
                self.velocity = int(f)
            if pressed.get(pygame.K_RIGHT) and self.rect.x + self.rect.width < 1024:
                self.move_right()
            if pressed.get(pygame.K_LEFT) and self.rect.x > 0:
                self.move_left()
            if pressed.get(pygame.K_UP) and self.rect.y > 0:
                self.move_up()
            if pressed.get(pygame.K_DOWN) and self.rect.y + self.rect.height < 768:
                self.move_down()

            if (pressed.get(pygame.K_RIGHT) and pressed.get(pygame.K_UP)) or (pressed.get(pygame.K_RIGHT) and pressed.get(pygame.K_DOWN)) or (pressed.get(pygame.K_LEFT) and pressed.get(pygame.K_UP)) or (pressed.get(pygame.K_LEFT) and pressed.get(pygame.K_DOWN)):
                self.velocity = int(f/0.7)
        
        
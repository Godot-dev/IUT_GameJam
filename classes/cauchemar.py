import pygame
from classes.player import Player
from classes.projectile import Projectile
from classes.typesProjectiles.pomme import Pomme

class Cauchemar:
    def __init__(self, difficulty, legumes):
        self.player = Player()    
        self.difficulty = difficulty
        self.liste_projectiles = pygame.sprite.Group()
        self.i = 1 # Permets de créer un nouveau projectile à l'écran tous les x temps

    def drawCauchemar(self, screen):
        screen.blit(self.player.image, self.player.rect)
        screen.blit(self.player.imageVie, (950,700))
        self.i += 1
        if self.i == 30:
            self.liste_projectiles.add(Pomme(self))
            self.i = 0
        for projectile in self.liste_projectiles:
            projectile.move()
            if projectile.rect.x < - projectile.rect.width or projectile.rect.x > 1024 + projectile.rect.width or projectile.rect.y < 0 - projectile.rect.y or projectile.rect.y > 768 + projectile.rect.y:
                projectile.nettoyage() # A rajouter à la fin de tous les move pour supprimer le projectile, s'il n'est plus sur l'écran
            elif self.check_collision(self.player,self.liste_projectiles):
                projectile.nettoyage()
                self.player.health -= 1
                if self.player.health == 2:
                    self.player.imageVie = pygame.image.load('assets/2coeurs.png')
                elif self.player.health == 1:
                    self.player.imageVie = pygame.image.load('assets/1coeurs.png')
                else: # Le joueur perds la partie, il faudra remplir plus tard le else
                    pass

        self.liste_projectiles.draw(screen)

    def catch_signal(self, pressed):
        f = self.player.velocity
        # Si le joueur va en diagonale, sa vitesse doit être réduite car il va faire deux déplacements en une seule action
        if (pressed.get(pygame.K_RIGHT) and pressed.get(pygame.K_UP)) or (pressed.get(pygame.K_RIGHT) and pressed.get(pygame.K_DOWN)) or (pressed.get(pygame.K_LEFT) and pressed.get(pygame.K_UP)) or (pressed.get(pygame.K_LEFT) and pressed.get(pygame.K_DOWN)):
            f *= 0.7
            self.player.velocity = int(f)

        if pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < 1024:
            self.player.move_right()
        if pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        if pressed.get(pygame.K_UP) and self.player.rect.y > 0:
            self.player.move_up()
        if pressed.get(pygame.K_DOWN) and self.player.rect.y + self.player.rect.height < 768:
            self.player.move_down()

        # Sa vitesse peut désormais être remise par défaut
        if (pressed.get(pygame.K_RIGHT) and pressed.get(pygame.K_UP)) or (pressed.get(pygame.K_RIGHT) and pressed.get(pygame.K_DOWN)) or (pressed.get(pygame.K_LEFT) and pressed.get(pygame.K_UP)) or (pressed.get(pygame.K_LEFT) and pressed.get(pygame.K_DOWN)):
            self.player.velocity = int(f/0.7)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask)

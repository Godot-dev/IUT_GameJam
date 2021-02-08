import pygame
import random
from classes.player import Player
from classes.projectile import Projectile
from classes.typesProjectiles.pomme import Pomme
from classes.typesProjectiles.salade import Salade
from classes.typesProjectiles.banane import Banane
from classes.typesProjectiles.poireau import Poireau
from classes.typesProjectiles.radis import Radis
from classes.typesProjectiles.citrouille import Citrouille
from classes.typesProjectiles.carotte import Carotte
from classes.typesProjectiles.cerise import Cerise
from classes.typesProjectiles.raisin import Raisin

class Cauchemar:
    def __init__(self, difficulty, legumesFruits):
        self.player = Player()    
        self.difficulty = difficulty
        self.liste_projectiles = pygame.sprite.Group()
        self.i = 1 # Permets de créer un nouveau projectile à l'écran tous les x temps
        self.MAX = 30 # Le MAX devra être changé en fonction de la difficulté
        self.legumesFruits = ["Poireau", "Raisin", "Carotte"]
        self.cooldownDash = 120 # Permets de ne pas autoriser le joueur de faire des dash à l'infini mais toutes les deux secondes

    def drawCauchemar(self, screen):
        screen.blit(self.player.image, self.player.rect)
        
        self.i += 1
        if self.i == self.MAX:
            j = random.randint(0,2) # sélectionne l'un des trois legumes/fruits du cauchemar
            self.liste_projectiles.add(globals()[self.legumesFruits[j]](self)) # et l'ajoute à l'écran
            self.i = 0
        for projectile in self.liste_projectiles:
            projectile.move()
            if projectile.rect.x < 0 or projectile.rect.x > 1024 or projectile.rect.y < 0 or projectile.rect.y > 768: 
                projectile.supprimer() # A rajouter à la fin de tous les move pour supprimer le projectile, s'il n'est plus sur l'écran
            elif self.check_collision(self.player,self.liste_projectiles):
                projectile.supprimer()
                self.player.health -= 1
                if self.player.health == 2:
                    self.player.imageVie = pygame.image.load('assets/2coeurs.png')
                elif self.player.health == 1:
                    self.player.imageVie = pygame.image.load('assets/1coeurs.png')
                else: # Le joueur perds la partie, il faudra remplir plus tard le else
                    pass

        self.liste_projectiles.draw(screen)
        screen.blit(self.player.imageVie, (950,700))

    def catch_signal(self, pressed):
        f = self.player.velocity
        self.cooldownDash += 1
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
        if pressed.get(pygame.K_SPACE) and self.cooldownDash > 120:
            self.player.dash(pressed)
            self.cooldownDash = 0 # On remets le cooldown à 0, il faudra donc attendre deux secondes (60*2 = 120) pour en effectuer un à nouveau 

        # Sa vitesse peut désormais être remise par défaut
        if (pressed.get(pygame.K_RIGHT) and pressed.get(pygame.K_UP)) or (pressed.get(pygame.K_RIGHT) and pressed.get(pygame.K_DOWN)) or (pressed.get(pygame.K_LEFT) and pressed.get(pygame.K_UP)) or (pressed.get(pygame.K_LEFT) and pressed.get(pygame.K_DOWN)):
            self.player.velocity = int(f/0.7)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask)

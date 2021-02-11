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
pygame.mixer.init

class Cauchemar:
    def __init__(self, difficulty, legumesFruits, game):
        self.difficulty = difficulty
        self.legumesFruits = legumesFruits
        self.images = self.loadImagesEnnemis()
        self.game = game
        self.player = Player()    
        self.background = pygame.image.load(f'assets/backgroundD{difficulty}.jpg')
        self.background = pygame.transform.scale(self.background, (1024, 768))
        self.liste_projectiles = []
        self.time = 0 # Indique le nombre de frames effectuées dans le cauchemar depuis son début
        self.frequence = 75 - difficulty * 15 # La fréquence à laquelle on crée un ennemi
        self.cooldownDash = 120 # Permets de ne pas autoriser le joueur de faire des dash à l'infini mais toutes les deux secondes

    def drawCauchemar(self, screen):
        screen.blit(self.background, (0,0))
        screen.blit(self.player.image, self.player.rect)
        self.time += 1
        if self.time % self.frequence == 0: # On ajoute un ennemi tous les self.frequence frames
            j = random.randint(0,2) # sélectionne l'un des trois legumes/fruits du cauchemar
            self.liste_projectiles.append(globals()[self.legumesFruits[j]](self.difficulty, self.images[j])) # et l'ajoute à l'écran
        
        for projectile in self.liste_projectiles:
            projectile.move()
            
            screen.blit(projectile.image,projectile.rect) 
            if(projectile.__class__.__name__ == "Carotte" and projectile.time > 120 and projectile.time < 180):
                pygame.draw.rect(screen,(255,255,255),projectile.bar_position)

            if projectile.rect.x + projectile.rect.w < 0  or projectile.rect.x - projectile.rect.w > 1024 or projectile.rect.y + projectile.rect.h < 0 or projectile.rect.y - projectile.rect.h > 768: 
                self.liste_projectiles.remove(projectile)
            elif self.check_collision(projectile):
                self.liste_projectiles.remove(projectile)
                self.player.health -= 1
                if self.player.health == 2:
                    pygame.mixer.Sound.play(pygame.mixer.Sound('assets/music/SoundFX/Hit1.ogg'))
                    self.player.imageVie = pygame.image.load('assets/2coeurs.png')
                elif self.player.health == 1:
                    pygame.mixer.Sound.play(pygame.mixer.Sound('assets/music/SoundFX/Hit1.ogg'))
                    self.player.imageVie = pygame.image.load('assets/1coeurs.png')
                else: # Le joueur perds la partie, il faudra remplir plus tard le else
                    pygame.mixer.Sound.play(pygame.mixer.Sound('assets/music/SoundFX/Hit1.ogg'))
                    self.game.perdu = True # Permettra de charger la bonne cinématique de défaite
                    self.terminerCauchemar()
        self.updateTimeBar(screen)
        if self.cooldownDash < 120:
            self.updateDashBar(screen)
        screen.blit(self.player.imageVie, (884,670))
        

    def catch_signal(self, pressed):
        f = self.player.velocity
        self.cooldownDash += 1
        diagonale = (pressed.get(pygame.K_RIGHT) and pressed.get(pygame.K_UP)) or (pressed.get(pygame.K_RIGHT) and pressed.get(pygame.K_DOWN)) or (pressed.get(pygame.K_LEFT) and pressed.get(pygame.K_UP)) or (pressed.get(pygame.K_LEFT) and pressed.get(pygame.K_DOWN))
        immobile = True # On ne sait pas encore si le joueur bouge, on part donc du principe qu'il est immobile
        # Si le joueur va en diagonale, sa vitesse doit être réduite car il va faire deux déplacements en une seule action
        if (diagonale): # Si le joueur se déplace quelque part en diagonale
            f *= 0.7
            self.player.velocity = int(f)

        if pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < 1024:
            self.player.move_right()
            immobile = False
        if pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
            immobile = False
        if pressed.get(pygame.K_UP) and self.player.rect.y > 0:
            self.player.move_up()
            immobile = False
        if pressed.get(pygame.K_DOWN) and self.player.rect.y + self.player.rect.height < 768:
            self.player.move_down()
            immobile = False
        if pressed.get(pygame.K_SPACE) and self.cooldownDash > 120 and not diagonale and not immobile:
            pygame.mixer.Sound.play(pygame.mixer.Sound('assets/music/SoundFX/Dash1.wav'))
            self.player.dash(pressed)
            self.cooldownDash = 0 # On remets le cooldown à 0, il faudra donc attendre deux secondes (60*2 = 120) pour en effectuer un à nouveau 

        # Sa vitesse peut désormais être remise par défaut
        if (diagonale):
            self.player.velocity = int(f/0.7)

    def check_collision(self, projectile):
        if(projectile.__class__.__name__ == "Carotte" and projectile.time > 120 and projectile.time < 180):
            return self.player.rect.colliderect(projectile.bar_position)
        else:
            return pygame.sprite.collide_mask(self.player, projectile)

    def updateTimeBar(self, screen):
        bar_back_color = (60,63,60) # Couleur de fond
        bar_color = (111,210,46) # Couleur affichant l'avancée du niveau

        bar_back_position = [30, 730, 128, 10]
        l = self.time / 30
        bar_position = [30, 730, l, 10]

        pygame.draw.rect(screen,bar_back_color,bar_back_position)
        pygame.draw.rect(screen,bar_color,bar_position)

        if(l == 16): # Le niveau est terminé
            if self.difficulty == 3: # Si le joueur vient de finir le dernier niveau, alors on informe game qui se chargera de finir le jeu
                self.game.victoire = True 
            self.terminerCauchemar()

    def updateDashBar(self, screen):
        bar_back_color = (60,63,60) # Couleur de fond
        bar_color = (111,210,46) # Couleur affichant l'avancée du niveau

        bar_back_position = [448, 730, 128, 10]
        bar_position = [448, 730, self.cooldownDash, 10]

        pygame.draw.rect(screen,bar_back_color,bar_back_position)
        pygame.draw.rect(screen,bar_color,bar_position)

    def terminerCauchemar(self):
        self.game.finCauchemar = True
        self.game.phaseDeJeu = None
    
    def loadImagesEnnemis(self):
        return [pygame.image.load(f'assets/projectiles/{self.legumesFruits[0]}.png'),pygame.image.load(f'assets/projectiles/{self.legumesFruits[1]}.png'),pygame.image.load(f'assets/projectiles/{self.legumesFruits[2]}.png')]
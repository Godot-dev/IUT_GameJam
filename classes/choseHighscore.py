import pygame
import json
import time
from classes.interface.button import Button
from classes.interface.borderRectangle import BorderRectangle

class ChoseHighscore:
    def __init__(self):
        # Image de background
        self.background =   pygame.image.load('assets/backgrounds/Highscore.png')
        self.menu =         Button(260, 107, 382, 650, 'assets/buttons/M.png')
        # Instanciation des éléments liés au menu des highscores
        self.pressed = {}
        self.default = True
        self.is_highscore = False
        self.is_writing = False
        self.text = "Pseudonyme"
        self.font = pygame.font.Font("assets/fonts/SegoeUI.ttf", 35)
        self.rect = self.font.render(self.text, True, (255, 255, 255)).get_rect()
        self.rect.topleft = (1024/2-237, 263)
        self.edittext = None
        self.cursor = pygame.Rect(self.rect.topright, (3, self.rect.height))
        self.set = False
        self.perdu = None
        self.health = None
        self.temps = None

    def setAttributes(self, perdu, health, temps):
        self.perdu = perdu
        self.health = health
        self.temps = temps
        self.set = True

    def drawHighscore(self, screen, display):
        screen.blit(self.background, (0, 0))
        screen.blit(self.menu.img, self.menu.hitbox)
        title = pygame.font.Font("assets/fonts/SegoeUI.ttf", 50).render("Entrez un pseudonyme si vous", 0, (255, 255, 255))
        h = title.get_height()
        screen.blit(title, (1024/2-title.get_width()/2, 50))
        title = pygame.font.Font("assets/fonts/SegoeUI.ttf", 50).render("voulez que le score soit sauvegardé !", 0, (255, 255, 255))
        screen.blit(title, (1024/2-title.get_width()/2, 50+h))     
        self.drawText(screen,display) 
            
    def drawText(self,screen,display):
        self.edittext = BorderRectangle(500, 75, 1024/2-250, 250, 3, (0, 0, 0, 255), (255, 255, 255), screen)
        img = self.font.render(self.text, True, (255, 255, 255))
        self.rect.size = img.get_size()
        self.cursor.topleft = self.rect.topright
        screen.blit(img, self.rect)
        if self.is_writing:
            if time.time() % 1 > 0.5:
                pygame.draw.rect(screen, (255, 255, 255), self.cursor)
            pygame.display.flip()
        
    def catch_signalC(self,event,screen,display):
        if self.is_writing:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if len(self.text)>0:
                        self.text = self.text[:-1]
                elif event.key == pygame.K_RETURN:
                    self.finishChoice()
                    self.is_writing = False
                    self.is_highscore = False
                elif event.key == pygame.K_ESCAPE:
                    if len(self.text)==0:
                        self.default = True
                        self.text = "Pseudonyme"
                    self.is_writing = False
                else:
                    if (15 > len(self.text)):
                        self.text += event.unicode
                self.drawText(screen, display)
            
    def catch_signalM(self,event,screen,display):
        if self.edittext.hitbox.collidepoint(event.pos):
            self.is_writing = True
            if self.default:
                self.text = ""
                self.drawText(screen, display)
            self.default = False
        else:
            self.is_writing = False
            if len(self.text)==0:
                self.default = True
                self.text = "Pseudonyme"
                self.drawText(screen, display)
        if self.menu.hitbox.collidepoint(event.pos):
            self.finishChoice()
            self.is_highscore = False
            self.is_writing = False

    def finishChoice(self):
        if len(self.text) != 0 and not self.default:
            with open('assets/properties/highscores.json') as fr:
                data = json.load(fr)
                if (self.perdu):
                    data['highscores'].append({"type":"lose", "name": self.text, "time": self.temps})
                else:
                    data['highscores'].append({"type":"win", "name": self.text, "heart": self.health})
                with open('assets/properties/highscores.json', 'w') as fw:
                    json.dump(data, fw)
        self.default = True
        self.is_highscore = False
        self.set = False
        self.perdu = None
        self.health = None
        self.temps = None
        self.text = "Pseudonyme"

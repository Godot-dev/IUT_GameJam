import pygame
import json
from classes.interface.button import Button
from classes.interface.borderRectangle import BorderRectangle

class Highscore:
    def __init__(self):
        # Image de background
        self.background =   pygame.image.load('assets/backgrounds/Highscore.png')
        self.menu =         Button(260, 107, 382, 650, 'assets/buttons/M.png')
        # Instanciation des éléments liés au menu des highscores
        self.is_highscore = False

    def drawHighscore(self,screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.menu.img, self.menu.hitbox)
        screen.blit(pygame.font.Font("assets/fonts/SegoeUI.ttf", 80).render("Highscores", 0, (255, 255, 255)), (315, 50))
        with open('assets/properties/highscores.json') as fr:
            data = json.load(fr)
            lenght = len(data['highscores'])
            if lenght > 0:
                for i in range(len(data['highscores'])):
                    tempHighscore = data['highscores'][i]
                    j = i
                    while j > 0 and self.compHighscore(tempHighscore, data['highscores'][j-1]):
                        data['highscores'][j] = data['highscores'][j-1]
                        j -= 1
                    data['highscores'][j] = tempHighscore
                i = 0
                for highscore in data['highscores']:
                    if (i == 5):
                        break
                    else:
                        if (i == 0):
                            color = (117, 115, 36, 255)
                            colorB = (74, 73, 21)
                            colorT = (255, 255, 255)
                        elif (i == 1):
                            color = (100, 100, 100, 255)
                            colorB = (50, 50, 50)
                            colorT = (255, 255, 255)
                        elif (i == 2):
                            color = (112, 72, 55, 255)
                            colorB = (66, 43, 32)
                            colorT = (255, 255, 255)
                        else:
                            color = (255, 255, 255, 255)
                            colorB = (255, 255, 255)
                            colorT = (0, 0, 0)

                        if (highscore['type'] == "win"):
                            textToDisplay = "Bravo " + highscore['name'] + " ! Vous avez gagné en ayant gardé " + str(highscore['heart']) + " coeurs !"
                        elif (highscore['type'] == "lose"):
                            textToDisplay = "Dommage " + highscore['name'] + "... Tu as perdu après avoir résisté " + str(highscore['time']) + " secondes."

                        textWithFont = pygame.font.Font("assets/fonts/SegoeUIItalic.ttf", 20).render(textToDisplay, 0, colorT)
                        textStart = 1024/2-textWithFont.get_width()/2
                        textTop = 260 + i*60

                        if (i == 0):
                            screen.blit(pygame.image.load('assets/backgrounds/first.png'), (textStart-90, textTop-10))
                        elif (i == 1):
                            screen.blit(pygame.image.load('assets/backgrounds/second.png'), (textStart-90, textTop-10))
                        elif (i == 2):
                            screen.blit(pygame.image.load('assets/backgrounds/third.png'), (textStart-90, textTop-10))

                        BorderRectangle(textWithFont.get_width()+40, 50, textStart-20, textTop-10, 3, color, colorB, screen)
                        screen.blit(textWithFont, (textStart, textTop))
                        i += 1
            else:
                screen.blit(pygame.font.Font("assets/fonts/SegoeUIItalic.ttf", 30).render("Vous n'avez pas encore joué de partie !", 0, (255, 255, 255)), (260, 250))
            
    def catch_signal(self,event):
        if self.menu.hitbox.collidepoint(event.pos):
            self.is_highscore = False
        
    def compHighscore(self, highscore1, highscore2): # Renvoie True si highscore 1 > highscore 2
        if (highscore1['type'] != highscore2['type']):
            if highscore1['type'] == "win":
                return True
            else:
                return False
        else:
            if highscore1['type'] == "lose":
                if highscore1['time'] >= highscore2['time']:
                    return True
                else:
                    return False
            else:
                if highscore1['heart'] >= highscore2['heart']:
                    return True
                else:
                    return False
            
        

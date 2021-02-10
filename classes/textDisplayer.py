import pygame
from threading import Thread
from queue import Queue

class TextDisplayer(Thread):
    def __init__(self, text, screen, display, type, font):
        Thread.__init__(self)
        self.text = text
        self.screen = screen
        self.display = display
        self.displaying = False
        if type == "notice":
            self.color = (77, 230, 39)
            self.fontTexte = pygame.font.Font('Arial', 24) # Application de la police
        else:
            self.color = (255, 255, 255)
            self.fontTexte = font

    def run(self):
        self.afficherTexte()
    
    def afficherTexte(self):
        mots = [mot.split(' ') for mot in self.text.splitlines()]  # Créé un tableau en 2D où chaque ligne est un tableau de mots
        esp = self.fontTexte.size(' ')[0]  # Largeur d'un espace
        largMax, hautMax = self.screen.get_size()
        largMax -= 45
        x, y = (45, 580)
        self.displaying = True
        for ligne in mots:
            for mot in ligne:
                surfMot = self.fontTexte.render(mot, 0, self.color)
                largMot, hautMot = surfMot.get_size()
                if x + largMot >= largMax:
                    x = 45  # Réinitialisation de x
                    y += hautMot  # Reprendre sur une nouvelle ligne
                for car in mot:
                    surfCaractere = self.fontTexte.render(car, 0, self.color)
                    largCar, hautCar = surfCaractere.get_size()
                    self.screen.blit(surfCaractere, (x, y))
                    if self.displaying:
                        self.display.flip()
                        pygame.time.delay(15)
                    x += largCar
                x += esp
            x = 45  # Réinitialisation de x
            y += hautMot  # Reprendre sur une nouvelle ligne
        self.displaying = False
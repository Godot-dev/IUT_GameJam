import pygame
import json
from classes.novelDialog import NovelDialog

class VisualNovel:
    def __init__(self, file, screen, display):
        # Définition de la police
        self.fontTexte = pygame.font.Font("assets/fonts/font.ttf", 24)
        self.fontNom = pygame.font.Font('assets/fonts/fontBold.ttf', 32)

        # Remplissage des attributs
        self.listDialog = []
        self.getElementsFromFile(file)
        self.currentDialog = self.listDialog[0]

        # AFFICHAGE
        self.changeDialog(screen, display)

    def changeDialog(self, screen, display):
        # Background
        self.background = pygame.image.load(self.currentDialog.img)

        # Rectangle du nom
        s = pygame.Surface((250, 50), pygame.SRCALPHA)
        s.fill((0, 0, 0, 175))
        screen.blit(s, (30, 508))
        # Bordures du nom
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect(30, 508, 3, 50))
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect(30, 508, 250, 3))
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect(277, 508, 3, 50))
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect(30, 555, 250, 3))
        # Nom
        screen.blit(self.fontNom.render(self.currentDialog.name, 0, (255, 255, 255)), (40, 518))
        
        # Rectangle du texte
        s = pygame.Surface((964, 170), pygame.SRCALPHA)
        s.fill((0, 0, 0, 175))
        screen.blit(s, (30, 568))
        # Bordures du texte
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect(30, 568, 3, 170))
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect(30, 568, 964, 3))
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect(991, 568, 3, 170))
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect(30, 735, 964, 3))
        # Texte
        self.afficherTexte(self.currentDialog.text, screen, display)
        
    def afficherTexte(self, text, surf, display):
        mots = [mot.split(' ') for mot in text.splitlines()]  # Créé un tableau en 2D où chaque ligne est un tableau de mots
        esp = self.fontTexte.size(' ')[0]  # Largeur d'un espace
        largMax, hautMax = surf.get_size()
        largMax -= 45
        x, y = (45, 580)
        for ligne in mots:
            for mot in ligne:
                surfMot = self.fontTexte.render(mot, 0, (255, 255, 255))
                largMot, hautMot = surfMot.get_size()
                if x + largMot >= largMax:
                    x = 45  # Réinitialisation de x
                    y += hautMot  # Reprendre sur une nouvelle ligne
                for car in mot:
                    surfCaractere = self.fontTexte.render(car, 0, (255, 255, 255))
                    largCar, hautCar = surfCaractere.get_size()
                    surf.blit(surfCaractere, (x, y))
                    display.flip()
                    pygame.time.delay(15)
                    x += largCar 
                x += esp
            x = 45  # Réinitialisation de x
            y += hautMot  # Reprendre sur une nouvelle ligne

    def getElementsFromFile(self, file):
        with open(file, "r") as file:
            data = json.load(file)
            for pid, dialog in data["dialogs"].items():
                if (dialog['type'] == "text"):
                    newDialog = NovelDialog(pid, dialog['type'], dialog['img'], dialog['name'], dialog['text'], None, dialog['next'])
                    self.listDialog.append(newDialog)
                else:
                    print(f"La novel dialog numéro {pid} a une erreur de type")
                


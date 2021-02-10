import pygame
import json
from classes.novelDialog import NovelDialog
from classes.borderRectangle import BorderRectangle

class VisualNovel:
    def __init__(self, file, screen, display):
        # Définition de la police
        self.fontTexte = pygame.font.Font("assets/fonts/font.ttf", 24)
        self.fontNom = pygame.font.Font('assets/fonts/fontBold.ttf', 32)

        # Remplissage des attributs
        self.screen = screen
        self.display = display
        self.listDialog = []
        self.getElementsFromFile(file)
        self.currentDialog = self.listDialog[0]

        # AFFICHAGE
        self.drawDialog()

    def drawDialog(self):
        # Background
        self.screen.blit(pygame.transform.scale(pygame.image.load(self.currentDialog.img), (1024, 768)), (0, 0))
        BorderRectangle(250, 50, 30, 508, 3, (0, 0, 0, 128), (255, 255, 255), self.screen)
        BorderRectangle(964, 170, 30, 568, 3, (0, 0, 0, 128), (255, 255, 255), self.screen)
        # Nom
        self.screen.blit(self.fontNom.render(self.currentDialog.name, 0, (255, 255, 255)), (40, 518))
        # Texte
        self.afficherTexte(self.currentDialog.text)
        
    def afficherTexte(self, text):
        mots = [mot.split(' ') for mot in text.splitlines()]  # Créé un tableau en 2D où chaque ligne est un tableau de mots
        esp = self.fontTexte.size(' ')[0]  # Largeur d'un espace
        largMax, hautMax = self.screen.get_size()
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
                    self.screen.blit(surfCaractere, (x, y))
                    self.display.flip()
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
                
    def catch_signal(self, pressed):
        if self.currentDialog.type == "text":
            if pressed.get(pygame.K_SPACE) or pressed.get(pygame.K_RETURN) or pressed.get("Clic"):
                if self.currentDialog.next == -1:
                    return True
                else:
                    self.currentDialog = self.listDialog[self.currentDialog.next]
                    self.drawDialog()
            
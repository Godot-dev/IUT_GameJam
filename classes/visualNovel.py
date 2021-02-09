import pygame

class VisualNovel:
    def __init__(self, file, screen):
        self.file = file
        self.fontTexte = pygame.font.Font("assets/fonts/font.ttf", 24)
        self.fontNom = pygame.font.Font('assets/fonts/fontBold.ttf', 32)
    
    def drawNovel(self, screen):
        # Rectangle du nom
        s = pygame.Surface((250, 50), pygame.SRCALPHA)
        s.fill((0, 0, 0, 128))
        screen.blit(s, (30, 508))
        # Bordures du nom
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect(30, 508, 3, 50))
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect(30, 508, 250, 3))
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect(277, 508, 3, 50))
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect(30, 555, 250, 3))
        # Nom
        screen.blit(self.fontNom.render("Marie-Christine", 0, (255, 255, 255)), (40, 518))
        # Rectangle du texte
        s = pygame.Surface((964, 170), pygame.SRCALPHA)
        s.fill((0, 0, 0, 128))
        screen.blit(s, (30, 568))
        # Bordures du texte
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect(30, 568, 3, 170))
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect(30, 568, 964, 3))
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect(991, 568, 3, 170))
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), pygame.Rect(30, 735, 964, 3))
        # Texte
        self.afficherMessage("Bonjour je m'appelle Marie-Christine et j'aime les pâtes mais pas mon prénom.", screen)
        
    def afficherMessage(self, text, surf):
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
                surf.blit(surfMot, (x, y))
                x += largMot + esp
            x = 45  # Réinitialisation de x
            y += hautMot  # Reprendre sur une nouvelle ligne

    def getText(self):
        pass


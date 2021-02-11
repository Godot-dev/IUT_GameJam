import pygame

class BorderRectangle:
    def __init__(self, width, height, posx, posy, border, color, borderColor, screen):
        # Rectangle
        self.width = width
        self.height = height
        self.surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.surf.fill(color)
        self.hitbox = pygame.Rect(posx+3, posy+3, self.surf.get_width()-6, self.surf.get_height()-6)
        screen.blit(self.surf, (posx, posy))
        # Bordures
        pygame.draw.rect(screen, borderColor, pygame.Rect(posx, posy, border, height))
        pygame.draw.rect(screen, borderColor, pygame.Rect(posx, posy, width, border))
        pygame.draw.rect(screen, borderColor, pygame.Rect(posx + width - border, posy, border, height))
        pygame.draw.rect(screen, borderColor, pygame.Rect(posx, posy + height - border, width, border))
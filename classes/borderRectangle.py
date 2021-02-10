import pygame

class BorderRectangle:
    def __init__(self, width, height, posx, posy, border, color, borderColor, screen):
        # Rectangle
        self.width = width
        self.height = height
        self.surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.surf.fill(color)
        self.hitbox = self.surf.get_rect()
        self.hitbox.x = posx
        self.hitbox.y = posy
        screen.blit(self.surf, (posx, posy))
        # Bordures
        pygame.draw.rect(screen, borderColor, pygame.Rect(posx, posy, border, height))
        pygame.draw.rect(screen, borderColor, pygame.Rect(posx, posy, width, border))
        pygame.draw.rect(screen, borderColor, pygame.Rect(posx + width - border, posy, border, height))
        pygame.draw.rect(screen, borderColor, pygame.Rect(posx, posy + height - border, width, border))
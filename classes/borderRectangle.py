import pygame

class BorderRectangle:
    def __init__(self, width, height, posx, posy, border, color, borderColor, screen):
        # Rectangle
        s = pygame.Surface((width, height), pygame.SRCALPHA)
        s.fill(color)
        screen.blit(s, (posx, posy))
        # Bordures
        pygame.draw.rect(screen, borderColor, pygame.Rect(posx, posy, border, height))
        pygame.draw.rect(screen, borderColor, pygame.Rect(posx, posy, width, border))
        pygame.draw.rect(screen, borderColor, pygame.Rect(posx + width - border, posy, border, height))
        pygame.draw.rect(screen, borderColor, pygame.Rect(posx, posy + height - border, width, border))
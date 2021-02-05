import pygame

pygame.init()

pygame.display.set_caption("Game")
screen = pygame.display.set_mode((1024, 768))

background = pygame.image.load('assets/0.png')

running = True

while running:
    screen.blit(background, (0, 0))

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


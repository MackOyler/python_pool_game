import pygame

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 678

#window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pool")

#loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
pygame.quit()
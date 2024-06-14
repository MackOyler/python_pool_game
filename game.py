import pygame
import pymunk
import pymunk.pygame_util

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 678

#window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pool")

#pm space
space = pymunk.Space()
draw_options = pymunk.pygame_util.DrawOptions(screen)

def create_ball(radius, pos):
    body = pymunk.Body()
    body.position = pos
    shape = pymunk.Circle(body, radius)
    shape.mass = 5
    
    space.add(body, shape)
    return shape

new_ball = create_ball(25, (300, 100))

#loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    space.debug_draw(draw_options)
    pygame.display.update()
            
pygame.quit()
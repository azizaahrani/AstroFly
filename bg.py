import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 560
screen_height = 660


bg = pygame.transform.scale(pygame.image.load('assets/bg3.png'), (screen_width, screen_height))
ground_img = pygame.transform.scale(pygame.image.load('assets/ground3.png'), (screen_width, 168))


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('AstroFly')

ground_scroll = 0
scroll_speed = 4

run = True
while run:

    clock.tick(fps)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(bg, (0, 0))

    screen.blit(ground_img, (ground_scroll, screen_height - 168))
    screen.blit(ground_img, (ground_scroll + screen_width, screen_height - 168))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) >= screen_width:
       
        ground_scroll = 0

    pygame.display.update()

pygame.quit()
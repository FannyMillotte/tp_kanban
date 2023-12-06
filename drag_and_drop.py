import pygame
import random

pygame.init()

# game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Drag And Drop')


items = []

for i in range(5):
    x = random.randint(50, 700)
    y = random.randint(50, 350)

    w = random.randint(35, 65)
    h = random.randint(35, 65)




run = True
while run :
    screen.fill('turquoise1')
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pass
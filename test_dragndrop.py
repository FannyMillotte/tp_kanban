# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:14:39 2023

@author: Claudia
"""

import pygame
from pygame.locals import *
from sys import exit

class Tache: 
    def __init__(self):
        self.description = "Test"
        
    def __str__(self):
        return "Tache : " + self.description
    


class Kanban:
    
    def __init__(self, noms_colonnes):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        self.nb_colonnes = 3
        self.noms_colonnes = noms_colonnes
        self.taches = [[Tache()],[Tache()],[Tache()]]
        self.color = (255,255,255)

# pygame setup
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

rect1 = Rect(50, 60, 200, 80)
rect2=rect1.copy()
x=0
y=0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            if event.type == KEYDOWN:
                 if event.key==K_LEFT:
                     x= -5
                     y=0
                 if event.key == K_RIGHT:
                     x=5
                     y=0
                 if event.key == K_UP:
                     x = 0
                     y = -5
                 if event.key == K_DOWN:
                     x = 0
                     y = 5

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    
    rect2.move_ip(x,y)
    screen.fill((127,127,127))
    pygame.draw.rect(screen, (255,0,0), rect1, 1)
    pygame.draw.rect(screen, (0,0,255), rect2, 5)
    pygame.display.update()
    pygame.display.flip()
    
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()


"""

    
        
    def afficher(self):

        for i in range(0, self.nb_colonnes):
            for j in range(0, 1):
                pygame.draw.rect(self.screen, self.color, Tache())
                
                
                
     pygame.init()
screen = pygame.display.set_mode((400,300))
rect1 = Rect(50, 60, 200, 80)
rect2=rect1.copy()
running = True
x=0
y=0
while running:
   for event in pygame.event.get():
      if event.type == QUIT:
         running = False
      if event.type == KEYDOWN:
         if event.key==K_LEFT:
            x= -5
            y=0
         if event.key == K_RIGHT:
            x=5
            y=0
         if event.key == K_UP:
            x = 0
            y = -5
         if event.key == K_DOWN:
            x = 0
            y = 5
   rect2.move_ip(x,y)
   screen.fill((127,127,127))
   pygame.draw.rect(screen, (255,0,0), rect1, 1)
   pygame.draw.rect(screen, (0,0,255), rect2, 5)
   pygame.display.update()
   pygame.quit()           
                
                
                
                
                
                
                
                
                
                
                """
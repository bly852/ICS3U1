import pygame, sys
from pygame.locals import *
import time

#Game Window Dimensions
w = 640
h = 480

#Base Cricle Measurements
x = int ((w/2))
y = int ((h/2))
r = 80

pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption ('pygame intro')
white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)

while True:
    screen.fill (pygame.Color (52, 235, 216))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        #Bottom Circle
        pygame.draw.circle(screen, white, (x,y+100), r)
        #Middle Circle
        pygame.draw.circle(screen, white, (x,y-20), r-20)
        #Top Circle
        pygame.draw.circle(screen, white, (x,y-110), r-40)
        #Left Eye
        pygame.draw.circle(screen, black, (x-10,y-130), r-75)
        #Right Eye
        pygame.draw.circle(screen, black, (x+10,y-130), r-75)
        #Nose
        pygame.draw.polygon(screen, pygame.Color(255,165,0), [(x-5,y-120), (x+5,y-120), (x,y-105)], 0)
        #Beads
        pygame.draw.circle(screen, black, (x,y-40), r-75)
        pygame.draw.circle(screen, black, (x,y-20), r-75)
        pygame.draw.circle(screen, black, (x,y), r-75)
        
        pygame.display.update()
        fpsClock.tick(60)
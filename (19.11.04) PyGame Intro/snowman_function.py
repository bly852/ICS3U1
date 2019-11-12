import pygame, sys, time
from pygame.locals import *

def drawSm(x,y,r):
    
    #Window Dimensions
    w = 640
    h = 480
    
    pygame.init()
    fpsClock = pygame.time.Clock()
    screen = pygame.display.set_mode((w,h))
    pygame.display.set_caption("Snowman Function")
    
    icon = pygame.image.load('stanley.png')
    pygame.display.set_icon(icon)
    
    while True:
        screen.fill (pygame.Color (52, 235, 216))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
                
        
        pygame.display.update()
        fpsClock.tick(60)
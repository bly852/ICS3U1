import pygame, sys, time
from pygame.locals import *

#Window Dimensions
w = 640
h = 480

pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((w,h))

icon = pygame.image.load('stanley.png')
pygame.display.set_caption("Snowman Function")
pygame.display.set_icon(icon)
    
#colours
white = pygame.Color(255,255,255)
black = pygame.Color(0,0,0)

def drawSm(x,y,r):
#Draws a snowman at a given location(x,y) with a given radius(r)
     
    r2 = int(r*1.25)
    r3 = int(r2*1.25)

    x += x_dir
    y += y_dir
    
    #Top Circle
    pygame.draw.circle(screen, white, (x,y), r)
    #Middle Circle
    pygame.draw.circle(screen, white, (x,y+r*2), r2)
    #Bottom Circle
    pygame.draw.circle(screen, white, (x,y+r*4), r3)
    
    
x_dir = 0
y_dir = 0

while True:
    screen.fill (pygame.Color (52, 235, 216))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT:
                x_dir = -5
            if event.key == K_RIGHT:
                x_dir = 5

    
    drawSm(240,150,50)
    
    pygame.display.update()
    fpsClock.tick(30)

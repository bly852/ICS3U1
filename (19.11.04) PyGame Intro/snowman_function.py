import pygame, sys, time, random
from pygame.locals import *

#Window Dimensions
w = 640
h = 480
x = w//2
y = 150
r = 50
x_dir = 0
y_dir = 0

flakes = []
for i in range (100):
    flakes.append([random.randint(1,w), random.randint(1,h), random.randint(1,5)])

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
    
    #Top Circle
    pygame.draw.circle(screen, white, (x,y), r)
    #Middle Circle
    pygame.draw.circle(screen, white, (x,y+r*2), r2)
    #Bottom Circle
    pygame.draw.circle(screen, white, (x,y+r*4), r3)
    

while True:
    screen.fill (pygame.Color (52, 235, 216))
    
    #Snowflakes
    for i in range (len(flakes)):
        pygame.draw.circle (screen, white, (flakes[i][0], flakes[i][1]), 6)
        flakes[i][1] = flakes[i][1] + flakes[i][2]
        if (flakes[i][1] > h ):
            flakes[i][1] = 0
            flakes[i][0] = random.randint(1,w)
        
    #Exiting Window
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            
            #Movement
            if event.key == K_LEFT:
                x_dir = -5
            if event.key == K_RIGHT:
                x_dir = 5
        if event.type == KEYUP:
            if event.key == K_LEFT:
                x_dir = 0
            if event.key == K_RIGHT:
                x_dir = 0
    
    #Edge Detection
    if x < w-w: 
        x_dir = 0
        x += 1
    if x > w: 
        x_dir = 0
        x -= 1
        
    drawSm(x,y,r)
    
    x += x_dir
    
    pygame.display.update()
    fpsClock.tick(60)
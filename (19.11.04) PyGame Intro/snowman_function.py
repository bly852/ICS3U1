import pygame, sys, time, random
from pygame.locals import *

#Window Dimensions
w = 640
h = 480

x = 240
y = 150
r = 50

x_dir = 0
y_dir = 0

rPlus = 0

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
    
    #Body (Top to Bottom)
    pygame.draw.circle(screen, white, (x,y), r)
    pygame.draw.circle(screen, white, (x,y+r*2), r2)
    pygame.draw.circle(screen, white, (x,y+r*4), r3)
     
    #Buttons (Top to Bottom)
    pygame.draw.circle(screen, black, (x,(y+r*2)-(r//2)), r//10)
    pygame.draw.circle(screen, black, (x,y+r*2), r//10)
    pygame.draw.circle(screen, black, (x,(y+r*2+(r//2))), r//10)
    
    #Eyes
    pygame.draw.circle(screen, black, (x-(r//3),y-(r//3)), r//10)
    pygame.draw.circle(screen, black, (x+(r//3),y-(r//3)), r//10)
    
    #Mouth (Left to Right)
    #pygame.draw.circle(screen, black,)

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
            
            if event.key == K_EQUALS:
                rPlus = 1
            if event.key == K_MINUS:
                rPlus = -1
            #Movement
            if event.key == K_LEFT or event.key == K_a:
                x_dir = -5
            if event.key == K_RIGHT or event.key == K_d:
                x_dir = 5
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT or event.key == K_a or event.key == K_d:
                x_dir = 0
            
            if event.key == K_EQUALS or event.key == K_MINUS:
                rPlus = 0
    
    r2 = int(r*1.25)
    r3 = int(r2*1.25)
    
    #Edge Detection
    if x < 0 + r3: 
        x_dir = 0
        x += 1
    elif x > w-r3: 
        x_dir = 0
        x -= 1
    if r == 0:
        r += 1
        
    drawSm(x,y,r)
    
    r += rPlus
    x += x_dir
    
    pygame.display.update()
    fpsClock.tick(60)
import pygame, sys, time, random
from pygame.locals import *

#Window Dimensions
w = 1368
h = 640

x = 240
y = 150
r = 50

x_dir = 0
y_dir = 0
rPlus = 0

floorY = h//10

flakes = []
for i in range ((w*h)//2500):
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
    
    #Floor
    pygame.draw.rect(screen, white, ((0, h-floorY), (w, h)), 0)
        
    #Key Detection
    for event in pygame.event.get():
        #Game Exit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        
        #Radius Change
        if event.type == KEYDOWN:
            if event.key == K_EQUALS:
                rPlus = 1
            if event.key == K_MINUS:
                rPlus = -1
        if event.type == KEYUP:
            if event.key == K_EQUALS or event.key == K_MINUS:
                rPlus = 0
        
        #Movement
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                x_dir = -7
            if event.key == K_RIGHT or event.key == K_d:
                x_dir = 7
            if event.key == K_UP or event.key == K_w or event.key == K_SPACE:
                if SmFoot >= h-floorY:
                    y -= 50
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT or event.key == K_a or event.key == K_d:
                x_dir = 0
    
    #Snowman Radiuses
    r2 = int(r*1.25)
    r3 = int(r2*1.25)
    SmHeight = r*2 + r2*2 + r3*2
    SmFoot = (SmHeight-(r2+r3)) + y
    
    #Edge Detection
    if x < 0 + r3: 
        x_dir = 0
        x += 1
    elif x > w-r3: 
        x_dir = 0
        x -= 1
    
    #Snowman Radius Error Prevention
    if r == 10:
        r += 1
    if SmHeight >= h-floorY:
        r -= 1
    
    #Gravity
    if SmFoot <= h-floorY:
        gravity = 8
    elif SmFoot >= h-floorY:
        gravity = 0
    if SmFoot > h-floorY+10:
        gravity = -16
        
    drawSm(x,y,r)
    
    r += rPlus
    x += x_dir
    y += gravity
    
    pygame.display.update()
    fpsClock.tick(60)
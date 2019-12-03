import pygame, sys
from pygame.locals import *

pygame.init()
x, y = 0, 300
a, b = 750, 300
s = 50
collidedLastFrame = False

width, height = 800, 600
windowSize = (width, height)
display = pygame.display.set_mode(windowSize)

dirx, diry, dira, dirb = 6, 4, 5, 7

clock = pygame.time.Clock()

def intersectsX(x1, x2, w1, w2):
    'return true if the x values intersect'
    if x1 >= x2 and x1 <= x2 + w2:
        return True
    if (x1 + w1) > x2 and (x1 + w1) <= (x2 + w2):
        return True
    return False

def intersectsY(y1, y2, h1, h2):
    'returns true if the y values intersect'
    if y1 >= y2 and y1 <= y2 + h2:
        return True
    if (y1 + h1) > y2 and (y1 + h1) <= (y2 + h2):
        return True
    return False
    
    
while True:
    
    for event in pygame.event.get():
        #Game Exit
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
    display.fill((0,0,0))
    
    rec1 = pygame.draw.rect(display, (0,255,0), (x, y, s, s))
    rec2 = pygame.draw.rect(display, (255,0,0), (a, b, s, s))
    
    intX = intersectsX(x, a, s, s)
    intY = intersectsY(y, b, s, s)
        
    if intX and intY == True:
        if (dirx < 0 and dira < 0) or (dirx > 0 and dira > 0):
            if dirx < dira:
                dira *= -1
            else:
                dirx *= -1
        if collidedLastFrame == False:
            dirx *= -1
            dira *= -1
            collidedLastFrame = True
    else:
        collidedLastFrame == False
    
    if x + s > width or x < 0:
        dirx *= -1
    if y + s > height or y < 0:
        diry *= -1
    if a + s > width or a < 0:
        dira *= -1
    if b + s > height or b < 0:
        dirb *= -1
    
    x += dirx
    y += diry
    a += dira
    b += dirb
    
    pygame.display.update()
    clock.tick(60)
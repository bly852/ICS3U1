#         course: ICS3U1 2019
#       exercise: Culminating Activity
#           date: 2019-12-06
# student number: 340926187
#           name: Brandon Ly
#    description: Two players (Mr Chun & Mr Pileggi) running around the school collecting food for the food drive.

import pygame, sys, time, random
from pygame.locals import *

# Colours
blue = (66, 144, 245)
red = (247, 59, 49)
green = (62, 247, 49)
white = (255, 255, 255)
black = (0, 0, 0)

# Window Dimensions
width = 1024
height = 576

# Pygame Startup
pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Culminating Assignment")

def randomColour():
    r, g, b = random.randint(0,255), random.randint(0,255), random.randint(0,255)
    colour = r, g, b
    return colour

# Player Class
class player:
    def __init__(self, colour, x, y, size):
        self.colour = colour
        self.x = x
        self.y = y
        self.size = size
        self.vel = 5
        self.hitbox = ()

    def draw (self, screen):
        pygame.draw.rect(screen, self.colour, ((self.x, self.y), (self.size, self.size)), 0)


class food:
    def __init__(self, randomColour, x, y, size):
        self.colour = randomColour
        self.x = x
        self.y = y
        self.size = 20

# players
player1 = player(green, 40, 100, 50)
player2 = player(red, 800, 200, 50)

# main loop
while True:
    screen.fill(white)

    # Exit Game
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and player1.y > player1.vel:
        player1.y -= player1.vel
    if keys[pygame.K_s] and player1.y < height - player1.size - player1.vel:
        player1.y += player1.vel
    if keys[pygame.K_a] and player1.x > player1.vel:
        player1.x -= player1.vel
    if keys[pygame.K_d] and player1.x < width - player1.size - player1.vel:
        player1.x += player1.vel

    if keys[pygame.K_UP] and player2.y > player2.vel:
        player2.y -= player2.vel
    if keys[pygame.K_DOWN] and player2.y < height - player2.size - player2.vel:
        player2.y += player2.vel
    if keys[pygame.K_LEFT] and player2.x > player2.vel:
        player2.x -= player2.vel
    if keys[pygame.K_RIGHT] and player2.x < width - player2.size - player2.vel:
        player2.x += player2.vel

    player1.draw(screen)
    player2.draw(screen)

    pygame.display.update()
    fpsClock.tick(60)
#         course: ICS3U1 2019
#       exercise: Culminating Activity
#           date: 2019-12-06
# student number: 340926187
#           name: Brandon Ly
#    description: Two players (Mr Chun & Mr Pileggi) running around the school collecting food for the food drive.

import pygame, random, os
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
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    colour = r, g, b
    return colour

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert()
        self.rect = self.image.get_rect()
        self.vel = 5
        self.rect.center = (width / 2, height / 2)


class Food:
    def __init__(self, randomColour, x, y, size):
        self.colour = randomColour
        self.x = x
        self.y = y
        self.size = 20


# sprite grouping
all_sprites = pygame.sprite.Group()

# players
player1 = Player('stanley.png')
all_sprites.add(player1)

# main loop
while True:
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

    all_sprites.update()

    screen.fill(white)
    all_sprites.draw(screen)

    fpsClock.tick(60)
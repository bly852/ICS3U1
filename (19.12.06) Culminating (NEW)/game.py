#         course: ICS3U1 2019
#       exercise: Culminating Activity
#           date: 2019-12-06
# student number: 340926187
#           name: Brandon Ly
#    description: Two players (Mr Chun & Mr Pileggi) running around the school collecting food for the food drive.

import pygame, sys
from pygame.locals import *
from settings import *

# pygame initialization
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_caption('Food Wars')
fpsClock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

# main loop
while True:
    fpsClock.tick(fps)
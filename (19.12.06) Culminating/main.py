#         course: ICS3U1 2019
#       exercise: Culminating Activity
#           date: 2019-12-06
# student number: 340926187
#           name: Brandon Ly
#    description: Two players (Mr Chun & Mr Pileggi) running around the school collecting food for the food drive.

# ██████╗ ██╗     
# ██╔══██╗██║     
# ██████╔╝██║     
# ██╔══██╗██║     
# ██████╔╝███████╗
# ╚═════╝ ╚══════╝

import pygame, sys, time
from pygame.locals import *

#Colours
blue = (66, 144, 245)
red = (247, 59, 49)
green = (62, 247, 49)
white = (255, 255, 255)
black = (0, 0, 0)

#Window Dimensions
width = 1024
height = 576

#pygame startup
pygame.init()
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Culminating Assignment")

#Player Class
class player:
    def draw (self, colour, x, y, size):
        pygame.draw.rect(screen, colour, ((x, y), (size, size)), 0)
    

#players
player1 = player()
player2 = player()


#main loop
while True:
    screen.fill(white)
    
    #Exit Game
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    player1.draw(green, 40, 100, 50)
    player2.draw(blue, 800, 200, 50)

    pygame.display.update()
    fpsClock.tick(60)
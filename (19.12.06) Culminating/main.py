#         course: ICS3U1 2019
#       exercise: Culminating Activity
#           date: 2019-12-06
# student number: 340926187
#           name: Brandon Ly
#    description: Two players (Mr Chun & Mr Pileggi) running around the school collecting food for the food drive.

import pygame, random, sys
from pygame.locals import *

# Colours
blue = (66, 144, 245)
red = (247, 59, 49)
green = (62, 247, 49)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
lightgrey = (100, 100, 100)

# Window Dimensions
width = 1024
height = 576

tileSize = 32
gridWidth = width / tileSize
gridHeight = height / tileSize

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((tileSize, tileSize))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, velX = 0, velY = 0):
        self.x += velX
        self.y += velY

    def update(self):
        self.rect.x = self.x * tileSize
        self.rect.y = self.y * tileSize

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((tileSize, tileSize))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

# game class
class Game():
    def __init__(self):
        # pygame startup
        pygame.init()
        fpsClock = pygame.time.Clock()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Culminating Assignment")

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.player = Player(self, 10, 10)
        for x in range(10, 20):
            Wall(self, x, 5)

    def run(self):
        self.running = True
        while self.running:
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

    def drawGrid(self):
        for x in range(0, width, tileSize):
            pygame.draw.line(self.screen, black, (x, 0), (x, height))
        for y in range(0, height, tileSize):
            pygame.draw.line(self.screen, black, (0, y), (width, y))

    def draw(self):
        self.screen.fill(white)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()



g = Game()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
    fpsClock.tick(60)
#         course: ICS3U1 2019
#       exercise: Culminating Activity
#           date: 2019-12-06
# student number: 340926187
#           name: Brandon Ly
#    description: Two players (Mr Chun & Mr Pileggi) running around the school collecting food for the food drive.

import pygame, random, sys
from pygame.locals import *
from settings import *
from sprites import *
from os import path
from map import *


class Game:
    def __init__(self):
        # initialize game window
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.fpsClock = pygame.time.Clock()
        pygame.key.set_repeat(1, 50)
        self.data_loader()

    def data_loader(self):
        game_folder = path.dirname(__file__)
        map_folder = path.join(game_folder, 'maps')
        self.map = Map(path.join(map_folder, 'biggerMap.txt'))

    def new(self):
        # new game loop
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == 'X':
                    Wall(self, col, row)
                if tile == "S":
                    self.player = Player(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.dt = self.fpsClock.tick(fps) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        # game loop - update
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, width, tileSize):
            pygame.draw.line(self.screen, lightgrey, (x, 0), (x, height))
        for y in range(0, height, tileSize):
            pygame.draw.line(self.screen, lightgrey, (0, y), (width, y))

    def draw(self):
        # game loop - draw
        self.screen.fill(black)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pygame.display.flip()

    def events(self):
        # game loop - events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.quit()

    def show_start_screen(self):
        # game start screen
        pass

    def show_game_over(self):
        # game over screen
        pass

game = Game()
game.show_start_screen()
while True:
    game.new()
    game.run()
    game.show_game_over()

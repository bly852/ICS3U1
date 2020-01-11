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
        self.fpsClock = pygame.time.Clock()
        self.data_loader()

    def data_loader(self):
        # loads paths for all assets
        game_folder = path.dirname(__file__)
        map_folder = path.join(game_folder, 'maps')
        image_folder = path.join(game_folder, 'images')
        food_folder = path.join(image_folder, 'food')
        self.food_image = pygame.image.load(path.join(food_folder, 'baconcheeseburger1.png'))
        self.map = Map(path.join(map_folder, 'biggerMap.txt'))
        self.floor_image = pygame.image.load(path.join(image_folder, floor_image))
        self.wall_image = pygame.image.load(path.join(image_folder, wall_image))
        self.player_image = pygame.image.load(path.join(image_folder, player_image))

    def new(self):
        # new game loop
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.floor = pygame.sprite.Group()
        self.food = pygame.sprite.Group()
        self.camera = Camera(self.map.width, self.map.height)
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == 'X':
                    Wall(self, col, row)
                else:
                    Floor(self, col, row)
        for x in range((self.map.tileWidth*self.map.tileHeight)//food_spawn_rate):
            Food(self, random.randint(1, self.map.tileWidth-2), random.randint(1, self.map.tileHeight-2))
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == "1":
                    Floor(self, col, row)
                    self.player = Player(self, col, row, 1)
                elif tile == "2":
                    Floor(self, col, row)
                    self.player = Player(self, col, row, 2)

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.dt = self.fpsClock.tick(fps) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        print("You got a score of {}!".format(self.player.score))
        pygame.quit()
        sys.exit()

    def update(self):
        # game loop - update
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw(self):
        # game loop - draw
        pygame.display.set_caption("{} | FPS: {:.0f}".format(title, self.fpsClock.get_fps()))
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

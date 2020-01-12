#         course: ICS3U1 2019
#       exercise: Culminating Activity
#           date: 2019-12-06
# student number: 340926187
#           name: Brandon Ly
#    description: Two players (Mr Chun & Mr Pileggi) running around the school collecting food for the food drive.

# main game script

import pygame, random, sys
from pygame.locals import *
from settings import *
from sprites import *
from os import path
from map import *
from gui import *


class Game:
    """
    Game class that contains the entire game
    """
    def __init__(self):
        """
        initialize pygame window when an instance is created
        """
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.fpsClock = pygame.time.Clock()
        self.data_loader()

    def data_loader(self):
        """
        loads paths to access game assets
        """
        game_folder = path.dirname(__file__)
        map_folder = path.join(game_folder, 'maps')
        image_folder = path.join(game_folder, 'images')
        self.map = Map(path.join(map_folder, 'biggerMap.txt'))
        self.floor_image = pygame.image.load(path.join(image_folder, floor_image))
        self.wall_image = pygame.image.load(path.join(image_folder, wall_image))
        self.player_image = pygame.image.load(path.join(image_folder, player_image))

    def new(self):
        """
        initializes a new game
        """
        # sprite groups to organize all sprites
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.floor = pygame.sprite.Group()
        self.food = pygame.sprite.Group()

        # initializes the camera for the player
        self.camera = Camera(self.map.width, self.map.height)

        # generates the map based on a text file given

        # generates walls and floors
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == 'X':
                    Wall(self, col, row)
                else:
                    Floor(self, col, row)

        # generates initial food sprites
        for x in range((self.map.tileWidth*self.map.tileHeight)//food_spawn_rate):
            Food(self, random.randint(0, self.map.tileWidth), random.randint(0, self.map.tileHeight))

        # generates player sprites
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == "1":
                    Floor(self, col, row)
                    self.player = Player(self, col, row, 1)
                elif tile == "2":
                    Floor(self, col, row)
                    self.player = Player(self, col, row, 2)

    def run(self):
        """
        main game loop
        """
        self.elapsed_time = 0
        self.foodTimer = 0
        while True:
            self.dt = self.fpsClock.tick(fps) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        """
        quits pygame and closes the window
        """
        print("You got a score of {}!".format(self.player.score))
        pygame.quit()
        sys.exit()

    def update(self):
        """
        part of the game loop - updates sprites
        """
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw(self):
        """
        part of the game loop - draws the new sprite positions
        and text to the screen
        """
        pygame.display.set_caption("{} | FPS: {:.0f} | Score: {}".format(title, self.fpsClock.get_fps(), self.player.score))

        # blit all sprites to the screen
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        # render and blit player score to the screen
        self.player_score = main_font.render(' Score: {}'.format(self.player.score), False, black)
        self.screen.blit(self.player_score, (0, 25))

        # rener and blit remaining time to the screen
        self.player_score = main_font.render(' Time Left: {} seconds'.format(time_limit-(int(self.elapsed_time))), False, black)
        self.screen.blit(self.player_score, (0, 0))

        # flip render to the screen
        pygame.display.flip()

    def events(self):
        """
        part of the game loop - checks for events
        """

        self.elapsed_time += self.dt
        if self.elapsed_time >= time_limit:
            self.quit()

        # adds delta time every frame to check how much time has passed since
        # a new food sprite has been spawned
        self.foodTimer += self.dt

        # generates new food sprites based on timer if the amount of food sprites
        # is less than amount of initial food sprites
        if len(self.food) < (self.map.tileWidth*self.map.tileHeight)//food_spawn_rate:
            if self.foodTimer > food_spawn_timer:
                Food(self, random.randint(0, self.map.tileWidth), random.randint(0, self.map.tileHeight))
                self.foodTimer = 0

        # checks for events to exit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.quit()

    def show_start_screen(self):
        """
        shows the games start screen
        """
        pass

    def show_game_over(self):
        """
        shows the game over screen
        """
        pass


game = Game()
game.show_start_screen()
while True:
    game.new()
    game.run()
    game.show_game_over()

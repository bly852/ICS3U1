#         course: ICS3U1 2019
#       exercise: Culminating Activity
#           date: 2019-12-06
# student number: 340926187
#           name: Brandon Ly
#    description: Two players (Mr Chun & Mr Pileggi) running around the school
#                 collecting food for the food drive.

# sprite classes

import pygame, random, os
from settings import *


class Player(pygame.sprite.Sprite):
    """
    player class that contains all data and functions related to the player
    """
    def __init__(self, game, x, y, player_num):
        """
        initalizes a player sprite when an instance is created in the game
        parameter,at the x and y paramters, and player num
        """
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_image
        self.image = pygame.transform.rotate(self.game.player_image, 90)
        self.rect = self.image.get_rect()
        self.velX, self.velY = 0, 0
        self.x = x * tileSize - tileSize
        self.y = y * tileSize - tileSize
        self.playerNum = player_num
        self.score = 0

    def get_keys(self):
        """
        checks for all keys pressed
        """
        self.velX, self.velY = 0, 0
        keys = pygame.key.get_pressed()
        if self.playerNum == 1:
            if keys[pygame.K_a]:
                self.velX = -player_speed
            if keys[pygame.K_d]:
                self.velX = player_speed
            if keys[pygame.K_w]:
                self.velY = -player_speed
            if keys[pygame.K_s]:
                self.velY = player_speed
        else:
            if keys[pygame.K_LEFT]:
                self.velX = -player_speed
            if keys[pygame.K_RIGHT]:
                self.velX = player_speed
            if keys[pygame.K_UP]:
                self.velY = -player_speed
            if keys[pygame.K_DOWN]:
                self.velY = player_speed

    def direction(self):
        """
        rotates the player sprite based on the current direction and new
        direction
        """
        if self.velX > 0:
            if self.velY < 0:
                self.image = pygame.transform.rotate(self.game.player_image, 45)
            elif self.velY > 0:
                self.image = pygame.transform.rotate(self.game.player_image, -45)
            else:
                self.image = pygame.transform.rotate(self.game.player_image, 0)
        elif self.velX < 0:
            if self.velY < 0:
                self.image = pygame.transform.rotate(self.game.player_image, 135)
            elif self.velY > 0:
                self.image = pygame.transform.rotate(self.game.player_image, -135)
            else:
                self.image = pygame.transform.rotate(self.game.player_image, 180)
        else:
            if self.velY < 0:
                self.image = pygame.transform.rotate(self.game.player_image, 90)
            elif self.velY > 0:
                self.image = pygame.transform.rotate(self.game.player_image, -90)

    def wall_collision(self, axis):
        """
        checks for player collision with the all wall sprites on the axis
        given and prevents player movement onto it
        """
        if axis == 'x':
            collides = pygame.sprite.spritecollide(self, self.game.walls, False)
            if collides:
                if self.velX > 0:
                    self.x = collides[0].rect.left - self.rect.width
                if self.velX < 0:
                    self.x = collides[0].rect.right
                self.velX = 0
                self.rect.x = self.x
        if axis == 'y':
            collides = pygame.sprite.spritecollide(self, self.game.walls, False)
            if collides:
                if self.velY > 0:
                    self.y = collides[0].rect.top - self.rect.height
                if self.velY < 0:
                    self.y = collides[0].rect.bottom
                self.velY = 0
                self.rect.y = self.y

    def food_collision(self):
        """
        checks for player collision with all food sprites killing any sprites it comes collides with and adding 1 to the players score value
        """
        collides = pygame.sprite.spritecollide(self, self.game.food, True)
        if collides:
            self.score +=1

    def update(self):
        """
        updates the players position
        """
        self.get_keys()
        self.direction()
        self.x += self.velX * self.game.dt
        self.y += self.velY * self.game.dt
        self.rect.x = self.x
        self.wall_collision('x')
        self.rect.y = self.y
        self.wall_collision('y')
        self.food_collision()


class Wall(pygame.sprite.Sprite):
    """
    class to contain all the data for wall sprites
    """
    def __init__(self, game, x, y):
        """
        initalizes a wall sprite when an instance is create in the game
        parameter, at the x and y paramters
        """
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * tileSize
        self.rect.y = y * tileSize

    def food_collision(self):
        """
        kills the food sprite if it collides with a wall sprite
        """
        collides = pygame.sprite.spritecollide(self, self.game.food, True)

    def update(self):
        """
        updates the wall sprite every frame
        """
        self.food_collision()


class Floor(pygame.sprite.Sprite):
    """
    class to contain all the data for floor sprites
    """
    def __init__(self, game, x, y):
        """
        initalizes a floor sprite when an instance is created in the game
        parameter, at the x and y paramters
        """
        self.groups = game.all_sprites, game.floor
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.floor_image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * tileSize
        self.rect.y = y * tileSize


class Food(pygame.sprite.Sprite):
    """
    class to contain all the data for food sprites
    """
    def __init__(self, game, x, y):
        """
        initalizes a food sprite when an instance is created in the game
        parameter, at the x and y paramters
        """
        self.groups = game.all_sprites, game.food
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        # picks random image for the sprite
        game_folder = os.path.dirname(__file__)
        image_folder = os.path.join(game_folder, 'images')
        food_folder = os.path.join(image_folder, 'food')
        self.image = pygame.image.load(os.path.join(food_folder ,(random.choice([
            x for x in os.listdir(food_folder)
                if os.path.isfile(os.path.join(food_folder, x))]))))

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * tileSize
        self.rect.y = y * tileSize

#         course: ICS3U1 2019
#       exercise: Culminating Activity
#           date: 2019-12-06
# student number: 340926187
#           name: Brandon Ly
#    description: Two players (Mr Chun & Mr Pileggi) running around the school
#                 collecting food for the food drive.

# sprite classes

import pygame
import random
import os
from settings import *


class Player(pygame.sprite.Sprite):
    """
    player class that contains all data and functions related to the player
    """

    def __init__(self, game, x, y, playerNum):
        """
        initalizes a player sprite when an instance is created in the game
        parameter,at the x and y paramters, and player num
        """
        self.playerNum = playerNum
        self.groups = game.all_sprites, game.players
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        if self.playerNum == 1:
            self.image = pygame.transform.rotate(self.game.player1_image, 90)
        else:
            self.image = pygame.transform.rotate(self.game.player2_image, 90)
        self.rect = self.image.get_rect()
        self.velX, self.velY = 0, 0
        self.x = x * tileSize - tileSize
        self.y = y * tileSize - tileSize

        self.score = 0

    def get_keys(self):
        """
        checks for all keys pressed and changes the players velocity on that axis to the player speed varaiable
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

        # if moving diagonally reduce the speed
        if self.velX > 0 and self.velY > 0:
            self.velX = player_speed * 0.701
            self.velY = player_speed * 0.701
        elif self.velX < 0 and self.velY < 0:
            self.velX = player_speed * -0.701
            self.velY = player_speed * -0.701



    def direction(self):
        """
        rotates the player sprite based on the current direction and new
        direction
        """
        if self.playerNum == 1:
            if self.velX > 0:
                if self.velY < 0:
                    self.image = pygame.transform.rotate(self.game.player1_image, 45)
                elif self.velY > 0:
                    self.image = pygame.transform.rotate(self.game.player1_image, -45)
                else:
                    self.image = pygame.transform.rotate(self.game.player1_image, 0)
            elif self.velX < 0:
                if self.velY < 0:
                    self.image = pygame.transform.rotate(self.game.player1_image, 135)
                elif self.velY > 0:
                    self.image = pygame.transform.rotate(self.game.player1_image, -135)
                else:
                    self.image = pygame.transform.rotate(self.game.player1_image, 180)
            else:
                if self.velY < 0:
                    self.image = pygame.transform.rotate(self.game.player1_image, 90)
                elif self.velY > 0:
                    self.image = pygame.transform.rotate(self.game.player1_image, -90)
        else:
            if self.velX > 0:
                if self.velY < 0:
                    self.image = pygame.transform.rotate(self.game.player2_image, 45)
                elif self.velY > 0:
                    self.image = pygame.transform.rotate(self.game.player2_image, -45)
                else:
                    self.image = pygame.transform.rotate(self.game.player2_image, 0)
            elif self.velX < 0:
                if self.velY < 0:
                    self.image = pygame.transform.rotate(self.game.player2_image, 135)
                elif self.velY > 0:
                    self.image = pygame.transform.rotate(self.game.player2_image, -135)
                else:
                    self.image = pygame.transform.rotate(self.game.player2_image, 180)
            else:
                if self.velY < 0:
                    self.image = pygame.transform.rotate(self.game.player2_image, 90)
                elif self.velY > 0:
                    self.image = pygame.transform.rotate(self.game.player2_image, -90)

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

    def player_collision(self, axis):
        """
        checks for player collision with the all wall sprites on the axis
        given and prevents player movement onto it
        """
        if self.playerNum == 1:
            if axis == 'x':
                if self.rect.colliderect(self.game.player2):
                    if self.velX > 0:
                        self.x = self.game.player2.rect.left - self.rect.width
                    if self.velX < 0:
                        self.x = self.game.player2.rect.right
                    self.velX = 0
                    self.rect.x = self.x
            if axis == 'y':
                if self.rect.colliderect(self.game.player2):
                    if self.velY > 0:
                        self.y = self.game.player2.rect.top - self.rect.height
                    if self.velY < 0:
                        self.y = self.game.player2.rect.bottom
                    self.velY = 0
                    self.rect.y = self.y

        else:
            if axis == 'x':
                if self.rect.colliderect(self.game.player1):
                    if self.velX > 0:
                        self.x = self.game.player1.rect.left - self.rect.width
                    if self.velX < 0:
                        self.x = self.game.player1.rect.right
                    self.velX = 0
                    self.rect.x = self.x
            if axis == 'y':
                if self.rect.colliderect(self.game.player1):
                    if self.velY > 0:
                        self.y = self.game.player1.rect.top - self.rect.height
                    if self.velY < 0:
                        self.y = self.game.player1.rect.bottom
                    self.velY = 0
                    self.rect.y = self.y

    def food_collision(self):
        """
        checks for player collision with all food sprites killing any sprites it comes collides with and adding 1 to the players score value
        """
        collides = pygame.sprite.spritecollide(self, self.game.food, True)
        if collides:
            self.score += 1

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
        self.player_collision('x')
        self.rect.y = self.y
        self.wall_collision('y')
        self.player_collision('y')
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
        self.image = pygame.image.load(os.path.join(food_folder, (random.choice([
            x for x in os.listdir(food_folder)
            if os.path.isfile(os.path.join(food_folder, x))]))))

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * tileSize
        self.rect.y = y * tileSize

        # checks if the sprite is allowed to spawn in the x and y
        self.spawnable = False
        collided = pygame.sprite.spritecollide(self, self.game.floor, False)
        for sprite in collided:
            if self.x == sprite.x and self.y == sprite.y:
                self.spawnable = True
        if self.spawnable == False:
            self.kill()

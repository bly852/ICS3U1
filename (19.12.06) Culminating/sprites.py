# sprite classes
import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y, player_num):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((tileSize, tileSize))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.velX, self.velY = 0, 0
        self.x = x * tileSize
        self.y = y * tileSize
        self.playerNum = player_num

    def get_keys(self):
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

    def wall_collision(self, axis):
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

    def update(self):
        self.get_keys()
        self.x += self.velX * self.game.dt
        self.y += self.velY * self.game.dt
        self.rect.x = self.x
        self.wall_collision('x')
        self.rect.y = self.y
        self.wall_collision('y')


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
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
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.floor
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.floor_image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * tileSize
        self.rect.y = y * tileSize

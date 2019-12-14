# sprite classes
import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((tileSize, tileSize))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

    def move(self, dirx = 0, diry = 0):
        if not self.wallCollision(dirx, diry):
            self.x += dirx
            self.y += diry

    def wallCollision(self, dirx, diry):
        for wall in self.game.walls:
            if wall.x == self.x + dirx and wall.y == self.y + diry:
                return True
        return False

    def update(self):
        self.rect.x = self.x * tileSize
        self.rect.y = self.y * tileSize

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((tileSize, tileSize))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * tileSize
        self.rect.y = y * tileSize

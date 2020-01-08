import pygame
from settings import *


class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as level:
            for line in level:
                self.data.append(line.strip())

        self.tileWidth = len(self.data[0])
        self.tileHeight = len(self.data)
        self.width = self.tileWidth * tileSize
        self.height = self.tileHeight * tileSize


class Camera:
    def __init__(self, cam_width, cam_height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = cam_width
        self.height = cam_height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.x + int(width / 2)
        y = -target.rect.y + int(height / 2)

        # camera limits
        x = min(0, x)
        y = min(0, y)
        x = max(-(self.width - width), x)
        y = max(-(self.height - height), y)
        self.camera = pygame.Rect(x, y, self.width, self.height)

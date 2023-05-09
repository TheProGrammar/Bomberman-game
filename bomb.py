import pygame


class Bomb:
    def __init__(self, x, y, tile_size, image):
        self.image = image
        self.tile_size = tile_size
        self.rect = self.image.get_rect(topleft=(x * tile_size, y * tile_size))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

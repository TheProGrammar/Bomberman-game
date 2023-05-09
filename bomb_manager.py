import pygame
from bomb import Bomb


class BombManager:
    def __init__(self, image_manager, tile_size):
        self.active_bombs = []
        self.image_manager = image_manager
        self.tile_size = tile_size
        self.bomb_image = self.image_manager.load_all_images()['bomb']

    def add_bomb(self, x, y):
        new_bomb = Bomb(x, y, self.tile_size, self.bomb_image)
        self.active_bombs.append(new_bomb)

    def draw_bombs(self, screen):
        for bomb in self.active_bombs:
            bomb.draw(screen)

    def update(self):
        # Here implement bomb-related logic such as explosion, timer, etc.
        pass

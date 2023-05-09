import pygame


class ImageManager:
    def __init__(self, tile_size):
        self.tile_size = tile_size

    def load_all_images(self):
        images = {
            'grass': pygame.transform.scale(pygame.image.load('grass_tile.png').convert_alpha(), (self.tile_size, self.tile_size)),
            'brick': pygame.transform.scale(pygame.image.load('brick_tile.png').convert_alpha(), (self.tile_size, self.tile_size)),
            'wall': pygame.transform.scale(pygame.image.load('wall_tile.png').convert_alpha(), (self.tile_size, self.tile_size)),
            'player': pygame.transform.scale(pygame.image.load('player_sprite.png').convert_alpha(), (self.tile_size, self.tile_size)),
            'bomb': pygame.transform.scale(pygame.image.load('bomb_sprite.png').convert_alpha(), (self.tile_size, self.tile_size)),
        }
        return images

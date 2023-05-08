class Tile:
    def __init__(self, x, y, image, tile_size, destructible, collision):
        self.image = image
        self.rect = image.get_rect(topleft=(x * tile_size, y * tile_size))
        self.destructible = destructible
        self.collision = collision

    def draw(self, screen):
        screen.blit(self.image, self.rect)

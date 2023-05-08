import pygame


class Player:
    def __init__(self, x, y, image, tile_size):
        self.image = image
        self.tile_size = tile_size
        self.rect = self.image.get_rect(topleft=(x * tile_size, y * tile_size))
        self.speed = 3

    def handle_input_and_move(self, keys, level):
        dx, dy = 0, 0
        old_rect = self.rect.copy()

        if keys[pygame.K_UP]:
            dy = -self.speed
        if keys[pygame.K_DOWN]:
            dy = self.speed
        if keys[pygame.K_LEFT]:
            dx = -self.speed
        if keys[pygame.K_RIGHT]:
            dx = self.speed

        # Update the player's rectangle position horizontally
        self.rect.x += dx

        # Check for horizontal collisions
        if level.check_collision(self.rect):
            self.rect.x = old_rect.x

        # Update the player's rectangle position vertically
        self.rect.y += dy

        # Check for vertical collisions
        if level.check_collision(self.rect):
            self.rect.y = old_rect.y

    def update(self, keys, level):
        self.handle_input_and_move(keys, level)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

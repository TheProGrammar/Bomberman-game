import pygame


class Player:
    def __init__(self, x, y, image_manager, tile_size):
        self.image_manager = image_manager
        self.image = self.image_manager.load_all_images()['player']
        self.tile_size = tile_size
        self.rect = self.image.get_rect(topleft=(x * tile_size, y * tile_size))
        self.speed = 3

    def handle_input_and_move(self, keys, level, bomb_manager):
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

        if keys[pygame.K_SPACE]:
            # Calculate the bomb position on the grid
            bomb_x = round(self.rect.x / self.tile_size)
            bomb_y = round(self.rect.y / self.tile_size)

            # Add a bomb through the bomb_manager
            bomb_manager.add_bomb(bomb_x, bomb_y)

    def update(self, keys, level, bomb_manager):
        self.handle_input_and_move(keys, level, bomb_manager)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
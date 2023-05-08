import sys

import pygame


class Player:
    def __init__(self, x, y, image, tile_size):
        self.x = x
        self.y = y
        self.image = image
        self.tile_size = tile_size
        self.rect = self.image.get_rect(topleft=(x * tile_size, y * tile_size))
        self.speed = 5
        self.dx = 0
        self.dy = 0

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.dy = -self.speed
            if event.key == pygame.K_DOWN:
                self.dy = self.speed
            if event.key == pygame.K_LEFT:
                self.dx = -self.speed
            if event.key == pygame.K_RIGHT:
                self.dx = self.speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.dy = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.dx = 0

        self.move(self.dx, self.dy)

    def move(self, dx, dy):
        # Update the player's rectangle position
        self.rect.x += dx
        self.rect.y += dy
        # Ensure the player stays within the screen bounds
        self.rect.x = max(0, min(self.rect.x, self.tile_size * 19 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, self.tile_size * 15 - self.rect.height))

    def update(self, event):
        self.handle_input(event)
        self.move(self.dx, self.dy)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

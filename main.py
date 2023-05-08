import pygame
import sys
from player import Player
from level import Level
from image_manager import ImageManager

# Initialize Pygame
pygame.init()

# Screen dimensions and tile size
TILE_SIZE = 64
SCREEN_WIDTH = 19 * TILE_SIZE
SCREEN_HEIGHT = 15 * TILE_SIZE

# Create the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption('Master Blaster')

# Initialize image manager
image_manager = ImageManager(TILE_SIZE)
images = image_manager.load_all_images()

# Initialize game objects
player = Player(1, 1, images['player'], TILE_SIZE)

# Initialize level objects
level = Level(TILE_SIZE)

clock = pygame.time.Clock()
speed = 5  # You can adjust this value to control the player's movement speed

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        player.update(event)

    # Draw level and player
    screen.fill((0, 0, 0))
    for y, row in enumerate(level.level_data):
        for x, tile in enumerate(row):
            if tile == 0:
                screen.blit(images['grass'], (x * TILE_SIZE, y * TILE_SIZE))
            elif tile == 1:
                screen.blit(images['brick'], (x * TILE_SIZE, y * TILE_SIZE))
            elif tile == 2:
                screen.blit(images['wall'], (x * TILE_SIZE, y * TILE_SIZE))
    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)

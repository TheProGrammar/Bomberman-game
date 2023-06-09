import pygame
import sys
from player import Player
from level import Level
from image_manager import ImageManager
from bomb_manager import BombManager

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
player = Player(1, 1, image_manager, TILE_SIZE)
bomb_manager = BombManager(image_manager, TILE_SIZE)
level = Level(TILE_SIZE, images)

# Create a font object for FPS counter
font = pygame.font.Font(pygame.font.get_default_font(), 24)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    player.update(keys, level, bomb_manager)
    bomb_manager.update()

    # Draw level and player
    level.draw(screen)
    player.draw(screen)
    bomb_manager.draw_bombs(screen)

    # Calculate and render FPS counter
    fps = int(clock.get_fps())
    fps_text = font.render(f'FPS: {fps}', True, (255, 255, 255))
    screen.blit(fps_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

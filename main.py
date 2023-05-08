import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions and tile size
TILE_SIZE = 64
SCREEN_WIDTH = 19 * TILE_SIZE
SCREEN_HEIGHT = 15 * TILE_SIZE

# Create the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Basic Pygame Project')


# Load images
def load_images():
    images = {
        'grass': pygame.transform.scale(pygame.image.load('grass_tile.png'), (TILE_SIZE, TILE_SIZE)),
        'brick': pygame.transform.scale(pygame.image.load('brick_tile.png'), (TILE_SIZE, TILE_SIZE)),
        'wall': pygame.transform.scale(pygame.image.load('wall_tile.png'), (TILE_SIZE, TILE_SIZE)),
        #'bomb': pygame.transform.scale(pygame.image.load('bomb_sprite.png'), (TILE_SIZE, TILE_SIZE)),
        'player': pygame.transform.scale(pygame.image.load('bomb_sprite.png'), (TILE_SIZE, TILE_SIZE))
    }
    return images

# Define the level (0 = grass, 1 = bricks, 2 = wall)
level = [
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
    [2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
    [2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
    [2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
    [2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 0, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    # ... Add more rows to complete the level
]


# Player class
class Player:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect(topleft=(x * TILE_SIZE, y * TILE_SIZE))

    def move(self, dx, dy):
        self.rect.move_ip(dx * TILE_SIZE, dy * TILE_SIZE)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Initialize game objects
images = load_images()
player = Player(1, 1, images['player'])

# Main game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move(0, -1)
            elif event.key == pygame.K_DOWN:
                player.move(0, 1)
            elif event.key == pygame.K_LEFT:
                player.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                player.move(1, 0)

    # Draw level and player
    screen.fill((0, 0, 0))
    for y, row in enumerate(level):
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

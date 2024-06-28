import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Set cell size
CELL_SIZE = 20

# Set game variables
snake_speed = 10
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, (SCREEN_WIDTH//CELL_SIZE)) * CELL_SIZE, 
            random.randrange(1, (SCREEN_HEIGHT//CELL_SIZE)) * CELL_SIZE]
food_spawn = True

# Set screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Set clock
clock = pygame.time.Clock()

# Define game functions
def draw_snake(snake_body):
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))

def draw_food(food_pos):
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Capture key press events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake_pos[1] -= CELL_SIZE
    if keys[pygame.K_DOWN]:
        snake_pos[1] += CELL_SIZE
    if keys[pygame.K_LEFT]:
        snake_pos[0] -= CELL_SIZE
    if keys[pygame.K_RIGHT]:
        snake_pos[0] += CELL_SIZE

    # Check for collision with food
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn new food
    if not food_spawn:
        food_pos = [random.randrange(1, (SCREEN_WIDTH//CELL_SIZE)) * CELL_SIZE, 
                    random.randrange(1, (SCREEN_HEIGHT//CELL_SIZE)) * CELL_SIZE]
        food_spawn = True

    # Move the snake
    snake_body.insert(0, list(snake_pos))

    # Draw everything
    screen.fill(BLACK)
    draw_snake(snake_body)
    draw_food(food_pos)
    pygame.display.update()

    # Check for game over conditions
    if snake_pos[0] < 0 or snake_pos[0] > SCREEN_WIDTH-CELL_SIZE or snake_pos[1] < 0 or snake_pos[1] > SCREEN_HEIGHT-CELL_SIZE:
        pygame.quit()
        sys.exit()

    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            pygame.quit()
            sys.exit()

    # Control snake speed
    clock.tick(snake_speed)

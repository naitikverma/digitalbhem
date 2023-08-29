import pygame
import sys
import random

pygame.init()

# Set up display
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20
CELL_WIDTH = WIDTH // CELL_SIZE
CELL_HEIGHT = HEIGHT // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize Snake and Food
snake = [(5, 5)]
snake_dir = (1, 0)
food = (CELL_WIDTH // 2, CELL_HEIGHT // 2)

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, 1):
                snake_dir = (0, -1)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -1):
                snake_dir = (0, 1)
            elif event.key == pygame.K_LEFT and snake_dir != (1, 0):
                snake_dir = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-1, 0):
                snake_dir = (1, 0)

    # Move snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, new_head)

    # Check for collision with food
    if snake[0] == food:
        food = (random.randint(0, CELL_WIDTH - 1), random.randint(0, CELL_HEIGHT - 1))
    else:
        snake.pop()

    # Check for collision with walls or itself
    if (
        new_head[0] < 0 or new_head[0] >= CELL_WIDTH or
        new_head[1] < 0 or new_head[1] >= CELL_HEIGHT or
        new_head in snake[1:]
    ):
        pygame.quit()
        sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw food
    pygame.draw.rect(screen, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
    clock.tick(10)  # Control the speed of the game

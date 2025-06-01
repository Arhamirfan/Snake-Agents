# File: snake_game_updated.py

import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Snake block size
BLOCK_SIZE = 20

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Snake class
class Snake:
    def __init__(self):
        self.size = 1
        self.elements = [[100, 100]]
        self.dir = [1, 0]  # Initial direction

    def get_head_position(self):
        return self.elements[0]

    def turn(self, point):
        if self.size > 1 and (point[0] * -1, point[1] * -1) == self.dir:
            return
        else:
            self.dir = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.dir
        new = [(cur[0] + (x * BLOCK_SIZE)) % SCREEN_WIDTH, (cur[1] + (y * BLOCK_SIZE)) % SCREEN_HEIGHT]
        if len(self.elements) > 2 and new in self.elements[2:]:
            self.reset()
        else:
            self.elements = [new] + self.elements[:-1]

    def reset(self):
        self.size = 1
        self.elements = [[100, 100]]
        self.dir = [1, 0]

    def draw(self):
        for element in self.elements:
            pygame.draw.rect(screen, GREEN, (element[0], element[1], BLOCK_SIZE, BLOCK_SIZE))

    def increase_size(self):
        self.size += 1
        self.elements.append([0, 0])

# Point class
class Point:
    def __init__(self):
        self.position = [random.randrange(1, (SCREEN_WIDTH // BLOCK_SIZE)) * BLOCK_SIZE,
                         random.randrange(1, (SCREEN_HEIGHT // BLOCK_SIZE)) * BLOCK_SIZE]

    def draw(self):
        pygame.draw.rect(screen, RED, (*self.position, BLOCK_SIZE, BLOCK_SIZE))

# Game loop
def game():
    snake = Snake()
    point = Point()
    running = True
    score = 0
    start_time = time.time()

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.turn([0, -1])
                elif event.key == pygame.K_DOWN:
                    snake.turn([0, 1])
                elif event.key == pygame.K_LEFT:
                    snake.turn([-1, 0])
                elif event.key == pygame.K_RIGHT:
                    snake.turn([1, 0])

        snake.move()
        snake.draw()
        point.draw()

        if snake.get_head_position() == point.position:
            point = Point()
            snake.increase_size()
            score += 1

        if score == 5 or time.time() - start_time > 50:
            running = False

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

game()
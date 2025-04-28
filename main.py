import pygame
from pygame.math import Vector2
import sys
import random


class SNAKE:
    def __init__(self, *args, **kwargs):
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
        self.direction = Vector2(1, 0)

    def draw_snake(self):
        for block in self.body:
            block_rect = pygame.Rect(
                block.x * cell_size, block.y * cell_size, cell_size, cell_size
            )
            pygame.draw.rect(screen, (50, 50, 50), block_rect)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]


class FRUIT:
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(
            self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size
        )
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)


class MAIN:
    def __init__(self, *args, **kwargs):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw_elements(self):
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            print("COLLIDING!")
            return True
        else:
            return False
        

pygame.init()

cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

snake = SNAKE()
fruit = FRUIT()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction != Vector2(0,1):
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction != Vector2(0,-1):
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction != Vector2(1,0):
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction != Vector2(-1,0):
                    main_game.snake.direction = Vector2(1, 0)

    screen.fill((175, 215, 70))
    main_game.draw_elements()

    pygame.display.update()
    clock.tick(60)

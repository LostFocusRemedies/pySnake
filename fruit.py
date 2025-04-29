import pygame
from pygame.math import Vector2
import random

class FRUIT:
    def __init__(self, cell_size, cell_number, screen):
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.screen = screen
        self.apple = pygame.image.load("assets/graphics/apple.png").convert_alpha()
        self.randomize()

    def randomize(self):
        self.x = random.randint(0, self.cell_number - 1)
        self.y = random.randint(0, self.cell_number - 1)
        self.pos = Vector2(self.x, self.y)

    def draw_fruit(self):
        fruit_rect = pygame.Rect(
            self.pos.x * self.cell_size, self.pos.y * self.cell_size, self.cell_size, self.cell_size
        )
        self.screen.blit(self.apple, fruit_rect)
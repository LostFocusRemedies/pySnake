import pygame
import pygame.locals
from pygame.math import Vector2

from snake import SNAKE
from fruit import FRUIT


class MAIN:
    def __init__(
        self, cell_size, cell_number, screen, game_font, SCREEN_UPDATE
    ):
        self.cell_size = cell_size
        self.cell_number = cell_number
        self.screen = screen
        self.game_font = game_font
        self.apple_image = pygame.image.load("assets/graphics/apple.png").convert_alpha() # that's for the score
        self.SCREEN_UPDATE = SCREEN_UPDATE

        self.snake = SNAKE(cell_size, screen)
        self.fruit = FRUIT(cell_size, cell_number, screen)
        self.speed = 250
        self.score = 0
        self.update_game_speed()

    def update_game_speed(self):
        game_speed = max(50, self.speed)
        pygame.time.set_timer(self.SCREEN_UPDATE, game_speed)

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()
            self.score += 1

            self.speed = max(50, 250 - (len(self.snake.body) * 5))
            self.update_game_speed()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if (
            not 0 <= self.snake.body[0].x <= self.cell_number - 1
            or not 0 <= self.snake.body[0].y <= self.cell_number - 1
        ):
            self.game_over()

        for block in self.snake.body[1:]:
            if self.snake.body[0] == block:
                self.game_over()

    def game_over(self):
        self.snake.reset()
        self.score = 0
        self.speed = 250
        self.update_game_speed()

    def draw_grass(self):
        grass_color = (167, 209, 61)
        for row in range(self.cell_number):
            if row % 2 == 0:
                for col in range(self.cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(
                            col * self.cell_size,
                            row * self.cell_size,
                            self.cell_size,
                            self.cell_size,
                        )
                        pygame.draw.rect(self.screen, grass_color, grass_rect)
            else:
                for col in range(self.cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(
                            col * self.cell_size,
                            row * self.cell_size,
                            self.cell_size,
                            self.cell_size,
                        )
                        pygame.draw.rect(self.screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = self.game_font.render(score_text, True, (56, 74, 12))
        score_x = int(self.cell_size * self.cell_number - 60)
        score_y = int(self.cell_size * self.cell_number - 60)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = self.apple_image.get_rect(
            midright=(score_rect.left, score_rect.centery)
        )
        bg_rect = pygame.Rect(
            apple_rect.left,
            apple_rect.top,
            apple_rect.width + score_rect.width + 6,
            apple_rect.height,
        )

        pygame.draw.rect(self.screen, (167, 209, 61), bg_rect)
        self.screen.blit(score_surface, score_rect)
        self.screen.blit(self.apple_image, apple_rect)
        pygame.draw.rect(self.screen, (56, 74, 12), bg_rect, 2)

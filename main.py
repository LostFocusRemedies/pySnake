from importlib import reload
import pygame
from pygame import Vector2
import sys
import game
reload(game)
from game import MAIN

def main():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    
    cell_size = 40
    cell_number = 20
    
    # Set up display
    screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
    pygame.display.set_caption("Snake Game")
    
    # Load resources
    clock = pygame.time.Clock()
    game_font = pygame.font.Font("assets/fonts/PoetsenOne-Regular.ttf", 25)
    
    # Define custom event for game updates
    SCREEN_UPDATE = pygame.USEREVENT
    
    # Create game instance
    main_game = MAIN(cell_size, cell_number, screen, game_font, SCREEN_UPDATE)
    
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == SCREEN_UPDATE:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.snake.direction != Vector2(0, 1):
                        main_game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction != Vector2(0, -1):
                        main_game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction != Vector2(1, 0):
                        main_game.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction != Vector2(-1, 0):
                        main_game.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_ESCAPE: 
                    quit_game()
    
        # Draw everything
        screen.fill((175, 215, 70))
        main_game.draw_elements()
    
        # Update display and control frame rate
        pygame.display.update()
        clock.tick(60)

def quit_game():
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
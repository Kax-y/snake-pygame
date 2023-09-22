"""
Snake Eater
Made with PyGame
"""
import pygame, sys
from snake.globals import *

# Checks for errors encountered
# pygame.init() example output -> (6, 0)
check_errors = pygame.init()

# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')

while True:
    for event in pygame.event.get():
        if_quit_then_exit(event)

    # Setup all controls for the game
    controls(event)    

    # Move the snake in the game window
    update_snake_position()

    # Food mechanic
    grow_snake()    
    spawn_food()

    # Drawing in the game window
    fill_background()
    draw_snake()
    draw_food()
    show_score(1, white, 'consolas', 20)

    # Game over conditions
    snake_out_of_bounds()
    snake_collision_with_itself()
    
    # Refresh game screen
    pygame.display.update()

    # Refresh rate
    fps_controller.tick(difficulty)
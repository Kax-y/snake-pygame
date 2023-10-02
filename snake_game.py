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

black, white, red, green, blue = init_colors()
difficulty = init_difficulty()
frame_size_x, frame_size_y = init_framesize()
fps_controller = init_fps_controller()

while True:
    for event in pygame.event.get():
        if_quit_then_exit(event)

    # Setup all controls for the game
    controls(event)    

    # Move the snake in the game window
    update_snake_position()

    # Food mechanic
    grow_snake()    
    spawn_food(frame_size_x, frame_size_y)

    # Drawing in the game window
    fill_background(black)
    draw_snake(green)
    draw_food(white)
    show_score(frame_size_x, frame_size_y, 1, white, 'consolas', 20)

    # Game over conditions
    game_over_conditions(frame_size_x, frame_size_y, black, red)
    
    # Refresh game screen
    pygame.display.update()

    # Refresh rate
    fps_controller.tick(difficulty)
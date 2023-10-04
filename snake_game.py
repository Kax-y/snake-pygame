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
frame_size_x, frame_size_y = init_framesize()
current_difficulty = 0

def main_game(difficulty):
    init_globals()
    global current_difficulty
    current_difficulty = difficulty
    while True:
        for event in pygame.event.get():
            if_quit_then_exit(event)

            # Setup all controls for the game
            controls(event)  

        # Move the snake in the game window
        update_snake_position()
        tmp = move_or_grow_snake(difficulty)
        if tmp != 0:
            current_difficulty = tmp

        # Food mechanic  
        spawn_food(frame_size_x, frame_size_y)

        # Drawing in the game window
        fill_background(black)
        draw_snake(green)
        draw_food(white)
        show_score(frame_size_x, frame_size_y, 1, white, 'consolas', 20)

        # Game over conditions
        if snake_out_of_bounds(frame_size_x, frame_size_y, black, red) == False:
            return
        if snake_collision_with_itself(frame_size_x, frame_size_y, black, red) == False:
            return
        
        # Refresh game screen
        pygame.display.update()

        # Refresh rate
        control_difficulty(current_difficulty)

while True:
    difficulty = menu(frame_size_x, frame_size_y, white, black)
    main_game(difficulty)

"""
Snake Eater
Made with PyGame
"""
import pygame, sys, time, random

# Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120
difficulty = 25

# Window size
frame_size_x = 720
frame_size_y = 480

# Checks for errors encountered
check_errors = pygame.init()
# pygame.init() example output -> (6, 0)
# second number in tuple gives number of errors
if check_errors[1] > 0:
    print(f'[!] Had {check_errors[1]} errors when initialising game, exiting...')
    sys.exit(-1)
else:
    print('[+] Game successfully initialised')


# Initialise game window
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))


# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255,255,0)


# FPS (frames per second) controller
fps_controller = pygame.time.Clock()


# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
food_spawn = True

direction = 'RIGHT'
new_direction = direction

score = 0
golden_apple_spawn = False
golden_apple_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
golden_apple_spawn_interval = 10
food_spawn_counter = 0


# Game Over
def game_over():
    """
    The the black screen that appears when the game is over. Consists of A text that reads "YOU DIED" and the players final score
    """
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()


# Score
def show_score(choice, color, font, size):
    """
    Shows the score both in-game and on the "Death screen"
    """
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x/10, 15)
    else:
        score_rect.midtop = (frame_size_x/2, frame_size_y/1.25)
    game_window.blit(score_surface, score_rect)
    # pygame.display.flip()
    




def if_quit_then_exit(event):
    """
    Quit the game if a quit event is given
    """
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


def movement_controls(event):
    """
    Set the 'W', 'A', 'S', 'D' keys as Up, Left, Down, Right respectively. This includes a check for legal direction.
    """
    new_direction = ""
    global direction

    if event.key == pygame.K_UP or event.key == ord('w'):
        new_direction = 'UP'
    if event.key == pygame.K_DOWN or event.key == ord('s'):
        new_direction = 'DOWN'
    if event.key == pygame.K_LEFT or event.key == ord('a'):
        new_direction = 'LEFT'
    if event.key == pygame.K_RIGHT or event.key == ord('d'):
        new_direction = 'RIGHT'
    
    if legal_direction(new_direction):
        direction = new_direction


def quit_key(event):
    """
    Set the 'ESC' key as exit key.
    """
    if event.key == pygame.K_ESCAPE:
        pygame.event.post(pygame.event.Event(pygame.QUIT))


def controls(event):
    """
    Movement controls (W, A, S, D).\n
    Exit (ESC).
    """
    # Whenever a key is pressed down
    if event.type == pygame.KEYDOWN:
        movement_controls(event)
        quit_key(event)


def legal_direction(new_direction):
    """
    Check if the direction is allowed, i.e. that the snake does not move in the opposite direction instantaneously.
    """
    if new_direction == 'UP' and direction != 'DOWN':
        return True
    if new_direction == 'DOWN' and direction != 'UP':
        return True
    if new_direction == 'LEFT' and direction != 'RIGHT':
        return True
    if new_direction == 'RIGHT' and direction != 'LEFT':
        return True
    
    return False


def update_snake_position():
    """
    Move the snake depending on current direction.
    """
    #TODO: Set position change as a constant instead of a magical number
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10


def grow_snake():
    """
    Increase snake size if food is eaten by snake
    """
    global score
    global food_spawn
    global food_spawn_counter
    global golden_apple_spawn
    global golden_apple_spawn_interval
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == golden_apple_pos[0] and snake_pos[1] == golden_apple_pos[1]:
        score += 3
        golden_apple_spawn = False
        food_spawn = False
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        #food_spawn_counter += 1
        food_spawn = False
        golden_apple_spawn = False
    else:
        snake_body.pop()

def spawn_food():
    """
    Spawn food if there is no food on the screen.
    """
    global food_spawn
    global food_pos
    global golden_apple_spawn
    global golden_apple_pos
    global food_spawn_counter
    global score

    print("food_spawn_counter:", food_spawn_counter)
    if not golden_apple_spawn and food_spawn_counter == 4:
        golden_apple_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
        golden_apple_spawn = True
    elif not food_spawn:
        food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
        food_spawn = True
        food_spawn_counter += 1
    

def draw_snake():
    """
    Draw the snake in the game window. One square at a time.
    """
    # TODO: Reoccuring magic number 10
    for pos in snake_body:
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))


def fill_background():
    """
    Fill the background with the colour black.
    """
    game_window.fill(black)
    

def draw_food():
    """
    Draw the existing food in the game window.
    """
    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

def draw_golden_apple():
    """
    Draw the existing food in the game window.
    """
    pygame.draw.rect(game_window, yellow, pygame.Rect(golden_apple_pos[0], golden_apple_pos[1], 10, 10))

def snake_out_of_bounds():
    """
    Show game over screen if the snake is outside the game window.
    """
    # Getting out of bounds
    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
        game_over()


def snake_collision_with_itself():
    """
    Show game over screen if snake walks into its tail.
    """
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()


# Main logic
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
    draw_golden_apple()
    show_score(1, white, 'consolas', 20)

    # Game over conditions
    snake_out_of_bounds()
    snake_collision_with_itself()
    
    # Refresh game screen
    pygame.display.update()

    # Refresh rate
    fps_controller.tick(difficulty)
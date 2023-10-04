import pygame, sys, time, random, pickle


def init_colors():
    """
    Initialize colors in (R, G, B)
    """
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)

    return black, white, red, green, blue


def init_framesize():
    """
    Initialize the framesize
    """
    frame_size_x = 720
    frame_size_y = 480

    return frame_size_x, frame_size_y


def init_fps_controller():
    """
    Initialize FPS (frames per second) controller
    """
    fps_controller = pygame.time.Clock()

    return fps_controller


# Initialise game window
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode(init_framesize())

GRID_SIZE = 10
DYNAMIC_DIFFICULTY_INCREASE = 3

def init_globals():
    """
    Initialize Snake values
    """

    global snake_pos, snake_body, food_pos, food_spawn, direction, score, fps_controller, new_direction
    
    fps_controller = init_fps_controller()

    snake_pos = [100, 50]
    snake_body = [[100, 50], [100-GRID_SIZE, 50], [100-(2*GRID_SIZE), 50]]

    food_pos = [random.randrange(1, (init_framesize()[0]//GRID_SIZE)) * GRID_SIZE, random.randrange(1, (init_framesize()[1]//GRID_SIZE)) * GRID_SIZE]
    food_spawn = True
    direction = 'RIGHT'
    new_direction = direction

    score = 0


def control_difficulty(difficulty):
    """
    Changing the time between frames. This controls the difficulty.
    """
    global fps_controller
    fps_controller.tick(difficulty)
    
# Game Over
def game_over(frame_size_x, frame_size_y, black, red):
    save_score()

    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    show_score(frame_size_x, frame_size_y, 0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    return False
    #pygame.quit()
    #sys.exit()


def show_score(frame_size_x, frame_size_y, choice, color, font, size):
    """
    Show score or highscore.\n
    Choice = 1: Show score.\n
    Choice = 0: Show highscores.
    """
    score_font = pygame.font.SysFont(font, size)
    
    if choice == 1:
        score_surface = score_font.render("Score: "  + str(score), True, color)
        score_rect = score_surface.get_rect()
        score_rect.midtop = (frame_size_x/10, 16)
        game_window.blit(score_surface, score_rect)

    elif choice == 0:
        render_list = []
        highscores = get_highscores()

        # Add highscore title to the highscore screen
        render_list.append("Highscores:")

        # Create each row of highscore
        for i in range(len(highscores)):
            render_list.append(str(i + 1) + ". " + str(highscores[i]))

        # Render the highscores in a list
        for i in range(len(render_list)):
            score_surface = score_font.render(render_list[i], True, color)
            score_rect = score_surface.get_rect()
            score_rect.midtop = (frame_size_x/2, frame_size_y/1.5 + 16 * i)
            game_window.blit(score_surface, score_rect)


def advance_difficulty(difficulty):
    """
    Increase the speed of the snake.
    """
    difficulty += DYNAMIC_DIFFICULTY_INCREASE
    return difficulty
    

def menu(frame_size_x, frame_size_y, white, black):
    """
    Display a menu for choosing game difficulty
    """

    my_font = pygame.font.SysFont('times new roman', 40)
    option_font = pygame.font.SysFont('times new roman', 30)

    title_surface = my_font.render('Snake Eater - Choose Difficulty', True, white)
    title_rect = title_surface.get_rect(center=(frame_size_x/2, frame_size_y/5))

    options = ["Easy", "Medium", "Hard", "Quit"]
    options_surfaces = [option_font.render(opt, True, white) for opt in options]
    options_rects = [surf.get_rect(center=(frame_size_x/2, frame_size_y/2 + i * 40)) for i, surf in enumerate(options_surfaces)]

    selected_index = 0

    menu_open = True
    difficulty_values = [10, 25, 40, -1]
    difficulty = difficulty_values[selected_index]

    while menu_open:
        for event in pygame.event.get():
            if_quit_then_exit(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and selected_index > 0:
                    selected_index -= 1
                elif event.key == pygame.K_DOWN and selected_index < len(options) - 1:
                    selected_index += 1
                elif event.key == pygame.K_RETURN:
                    difficulty = difficulty_values[selected_index]
                    menu_open = False

        game_window.fill(black)
        game_window.blit(title_surface, title_rect)

        for i, (opt_surf, opt_rect) in enumerate(zip(options_surfaces, options_rects)):
            if i == selected_index:
                pygame.draw.rect(game_window, white, opt_rect.inflate(20, 10), 2)  # Draw a white box around the selected option
            game_window.blit(opt_surf, opt_rect)

        pygame.display.flip()
    
    if difficulty == -1:
        sys.exit()

    return difficulty


def if_quit_then_exit(event):
    """
    Quit the game if a quit event is given.
    """
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


def save_score():
    """
    Save the 5 best scores in a pickle file.
    """
    #TODO: Add player names
    try:
        with open("highscores.pickle", "rb") as score_file:
            highscores = pickle.load(score_file)
    except:
        highscores = []

    highscores.append(score)
    highscores.sort(reverse=True)

    with open("highscores.pickle", "wb") as score_file:    
        pickle.dump(highscores[:5], score_file)


def get_highscores():
    """
    Get the top 5 highscores from a pickle file.
    """
    try:
        with open("highscores.pickle", "rb") as score_file:
            highscores = pickle.load(score_file)
    except:
        highscores = []

    return highscores


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
    if event.type != pygame.QUIT and event.type == pygame.KEYDOWN:
        movement_controls(event)
        quit_key(event)


def movement_controls(event):
    """
    Set the 'W', 'A', 'S', 'D' keys as Up, Left, Down, Right respectively. This includes a check for legal direction.
    """
    global new_direction

    if event.key == pygame.K_UP or event.key == ord('w'):
        new_direction = 'UP'
    if event.key == pygame.K_DOWN or event.key == ord('s'):
        new_direction = 'DOWN'
    if event.key == pygame.K_LEFT or event.key == ord('a'):
        new_direction = 'LEFT'
    if event.key == pygame.K_RIGHT or event.key == ord('d'):
        new_direction = 'RIGHT'


def update_direction_if_legal():
    """
    Check if the direction is allowed, i.e. that the snake does not move in the opposite direction instantaneously.
    """
    global new_direction, direction
    if new_direction == 'UP' and direction != 'DOWN':
        direction = new_direction
    elif new_direction == 'DOWN' and direction != 'UP':
        direction = new_direction
    elif new_direction == 'LEFT' and direction != 'RIGHT':
        direction = new_direction
    elif new_direction == 'RIGHT' and direction != 'LEFT':
        direction = new_direction


def update_snake_position():
    """
    Move the snake depending on current direction.
    """
    if direction == 'UP':
        snake_pos[1] -= GRID_SIZE
    if direction == 'DOWN':
        snake_pos[1] += GRID_SIZE
    if direction == 'LEFT':
        snake_pos[0] -= GRID_SIZE
    if direction == 'RIGHT':
        snake_pos[0] += GRID_SIZE


def move_or_grow_snake(difficulty):
    """
    Increase snake size if food is eaten by snake otherwise move the snake.
    """
    global score, food_spawn
    new_difficulty = difficulty

    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        new_difficulty = advance_difficulty(difficulty)
        food_spawn = False
        return new_difficulty
    
    else:
        snake_body.pop()

    return 0

    


def spawn_food(frame_size_x, frame_size_y):
    """
    Spawn food if there is no food on the screen.
    """
    global food_spawn
    global food_pos
    if not food_spawn:
        food_pos = [random.randrange(1, (frame_size_x//GRID_SIZE)) * GRID_SIZE, random.randrange(1, (frame_size_y//GRID_SIZE)) * GRID_SIZE]
    food_spawn = True


def draw_snake(green):
    """
    Draw the snake in the game window. One square at a time.
    """
    for pos in snake_body:
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], GRID_SIZE, GRID_SIZE))


def fill_background(black):
    """
    Fill the background with the colour black.
    """
    game_window.fill(black)
    

def draw_food(white):
    """
    Draw the existing food in the game window.
    """
    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], GRID_SIZE, GRID_SIZE))


def snake_out_of_bounds(frame_size_x, frame_size_y, black, red):
    """
    Show game over screen if the snake is outside the game window.
    """
    # Getting out of bounds
    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x - GRID_SIZE:
        return game_over(frame_size_x, frame_size_y, black, red)
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y - GRID_SIZE:
        return game_over(frame_size_x, frame_size_y, black, red)
    return True


def snake_collision_with_itself(frame_size_x, frame_size_y, black, red):
    """
    Show game over screen if snake walks into its tail.
    """
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            return game_over(frame_size_x, frame_size_y, black, red)
    return True
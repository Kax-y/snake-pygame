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


def init_difficulty():
    """
    Initialize difficulty for snake
    Easy      ->  10
    Medium    ->  25
    Hard      ->  40
    Harder    ->  60
    Impossible->  120
    """
    difficulty = 25
    
    return difficulty


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

# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_pos = [random.randrange(1, (init_framesize()[0]//10)) * 10, random.randrange(1, (init_framesize()[1]//10)) * 10]
food_spawn = True

direction = 'RIGHT'
new_direction = direction

score = 0


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
    time.sleep(5)
    pygame.quit()
    sys.exit()


def show_score(frame_size_x, frame_size_y, choice, color, font, size):
    """
    Show score or highscore.\n
    Choice = 1: Show score.\n
    Choice = 0: Show highscores.
    """
    score_font = pygame.font.SysFont(font, size)
    
    if choice == 1:
        score_surface = score_font.render("Score :"  + str(score), True, color)
        score_rect = score_surface.get_rect()
        score_rect.midtop = (frame_size_x/10, 16)
        game_window.blit(score_surface, score_rect)

    elif choice == 0:
        render_list = []
        highscores = get_highscores()
        print(highscores)

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


def if_quit_then_exit(event):
    """
    Quit the game if a quit event is given
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
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()


def spawn_food(frame_size_x, frame_size_y):
    """
    Spawn food if there is no food on the screen.
    """
    global food_spawn
    global food_pos
    if not food_spawn:
        food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(1, (frame_size_y//10)) * 10]
    food_spawn = True


def draw_snake(green):
    """
    Draw the snake in the game window. One square at a time.
    """
    # TODO: Reoccuring magic number 10
    for pos in snake_body:
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))


def fill_background(black):
    """
    Fill the background with the colour black.
    """
    game_window.fill(black)
    

def draw_food(white):
    """
    Draw the existing food in the game window.
    """
    pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))


def game_over_conditions(frame_size_x, frame_size_y, black, red):
    """
    Game over conditions.
    """
    snake_out_of_bounds(frame_size_x, frame_size_y, black, red)
    snake_collision_with_itself(frame_size_x, frame_size_y, black, red)


def snake_out_of_bounds(frame_size_x, frame_size_y, black, red):
    """
    Show game over screen if the snake is outside the game window.
    """
    # Getting out of bounds
    if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10:
        game_over(frame_size_x, frame_size_y, black, red)
    if snake_pos[1] < 0 or snake_pos[1] > frame_size_y-10:
        game_over(frame_size_x, frame_size_y, black, red)


def snake_collision_with_itself(frame_size_x, frame_size_y, black, red):
    """
    Show game over screen if snake walks into its tail.
    """
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over(frame_size_x, frame_size_y, black, red)
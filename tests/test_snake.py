import unittest
import snake.globals as snake
import pygame
import random


class TestSnake(unittest.TestCase):
    """
    Test relevant snake functionality.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialise necessary values for testing.
        """
        super(TestSnake, self).__init__(*args, **kwargs)
        self.difficulty = 10
        self.seed = 42
        random.seed(self.seed)
        snake.init_globals(self.difficulty)

    def setUp(self):
        """
        Reset global values
        """
        random.seed(self.seed)
        snake.init_globals(self.difficulty)

    def test_init_colors(self):
        """
        Check that all colours are initialised properly.
        """
        black, white, red, green, blue, yellow = snake.init_colors()

        self.assertEqual(black, pygame.Color(0, 0, 0))
        self.assertEqual(white, pygame.Color(255, 255, 255))
        self.assertEqual(red, pygame.Color(255, 0, 0))
        self.assertEqual(green, pygame.Color(0, 255, 0))
        self.assertEqual(blue, pygame.Color(0, 0, 255))
        self.assertEqual(yellow, pygame.Color(255, 255, 0))

    def test_init_framesize(self):
        frame_size_x, frame_size_y = snake.init_framesize()

        self.assertEqual(frame_size_x, 720)
        self.assertEqual(frame_size_y, 480)

    def test_init_fps_controller(self):
        """
        Check that the fps controller is initialised properly.
        """
        fps_controller = snake.init_fps_controller()

        self.assertIsInstance(fps_controller, pygame.time.Clock)

    def test_init_globals(self):
        """
        Test that the global values are initialised correctly.
        """
        FRAME_SIZE = snake.init_framesize()
        random.seed(self.seed)

        CORRECT_SNAKE_POSITION = [100, 50]
        CORRECT_SNAKE_BODY = [[100, 50], [
            100 - snake.GRID_SIZE, 50], [100 - (2 * snake.GRID_SIZE), 50]]
        CORRECT_FOOD_POSITION = [random.randrange(1, (FRAME_SIZE[0]//snake.GRID_SIZE)) * snake.GRID_SIZE,
                                 random.randrange(1, (FRAME_SIZE[1]//snake.GRID_SIZE)) * snake.GRID_SIZE]

        self.assertEqual(snake.snake_pos, CORRECT_SNAKE_POSITION)
        self.assertEqual(snake.snake_body, CORRECT_SNAKE_BODY)
        self.assertEqual(snake.food_pos, CORRECT_FOOD_POSITION)

        self.assertEqual(snake.food_spawn, True)
        self.assertEqual(snake.direction, snake.RIGHT)
        self.assertEqual(snake.score, 0)
        self.assertEqual(snake.new_direction, snake.RIGHT)
        self.assertEqual(snake.food_spawn_counter, 0)
        self.assertEqual(snake.obstacle_pos, [])
        self.assertEqual(snake.obs_spawn_counter, 0)
        self.assertEqual(snake.obstacle_spawn, 0)
        self.assertEqual(snake.difficulty, self.difficulty)

    def test_update_snake_position(self):
        """
        Test updating snake position.
        """
        # Move up
        snake.direction = snake.UP
        previous_pos = snake.snake_pos[1]
        snake.update_snake_position()
        self.assertTrue(snake.snake_pos[1], previous_pos - snake.GRID_SIZE)

        # Move down
        snake.direction = snake.DOWN
        previous_pos = snake.snake_pos[1]
        snake.update_snake_position()
        self.assertTrue(snake.snake_pos[1], previous_pos + snake.GRID_SIZE)

        # Move left
        snake.direction = snake.LEFT
        previous_pos = snake.snake_pos[0]
        snake.update_snake_position()
        self.assertTrue(snake.snake_pos[1], previous_pos - snake.GRID_SIZE)

        # Move right
        snake.direction = snake.RIGHT
        previous_pos = snake.snake_pos[0]
        snake.update_snake_position()
        self.assertTrue(snake.snake_pos[1], previous_pos + snake.GRID_SIZE)

    def test_save_get_score(self):
        """
        Test that a saved score is the same score when loaded.
        """
        TEST_SCORE = 8
        TEST_FILENAME = "test"

        snake.score = TEST_SCORE

        snake.save_score(TEST_FILENAME)
        highscores = snake.get_highscores(TEST_FILENAME)

        # Check that the saved score is the same as the one loaded
        self.assertEqual(highscores[0], TEST_SCORE)

        # Clear the test file
        open(f"{TEST_FILENAME}.pickle", 'w').close()

    def test_legal_direction_down(self):
        """
        Test one illegal and one legal new direction with down as starting direction
        """
        snake.direction = snake.DOWN
        snake.new_direction = snake.UP
        snake.update_direction_if_legal()
        self.assertEqual(snake.direction, snake.DOWN)

        snake.direction = snake.DOWN
        snake.new_direction = snake.UP
        snake.update_direction_if_legal()
        self.assertEqual(snake.direction, snake.DOWN)

    def test_legal_direction_up(self):
        """
        Test one illegal and one legal new direction with up as starting direction
        """
        snake.direction = snake.UP
        snake.new_direction = snake.DOWN
        snake.update_direction_if_legal()
        self.assertEqual(snake.direction, snake.UP)

        snake.direction = snake.DOWN
        snake.new_direction = snake.RIGHT
        snake.update_direction_if_legal()
        self.assertEqual(snake.direction, snake.RIGHT)

    def test_legal_direction_right(self):
        """
        Test one illegal and one legal new direction with right as starting direction
        """
        snake.direction = snake.RIGHT
        snake.new_direction = snake.LEFT
        snake.update_direction_if_legal()
        self.assertEqual(snake.direction, snake.RIGHT)

        snake.direction = snake.RIGHT
        snake.new_direction = snake.UP
        snake.update_direction_if_legal()
        self.assertEqual(snake.direction, snake.UP)

    def test_legal_direction_left(self):
        """
        Test one illegal and one legal new direction with left as starting direction
        """
        snake.direction = snake.LEFT
        snake.new_direction = snake.RIGHT
        snake.update_direction_if_legal()
        self.assertEqual(snake.direction, snake.LEFT)

        snake.direction = snake.LEFT
        snake.new_direction = snake.DOWN
        snake.update_direction_if_legal()
        self.assertEqual(snake.direction, snake.DOWN)


if __name__ == '__main__':
    unittest.main()

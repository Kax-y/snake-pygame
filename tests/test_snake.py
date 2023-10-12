import unittest
import snake.globals as snake
import pygame


class TestSnake(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSnake, self).__init__(*args, **kwargs)
        snake.init_globals()
        self.starting_food_pos = snake.food_pos
        self.starting_food_spawn = snake.food_spawn
        self.starting_food_spawn_counter = snake.food_spawn_counter
        self.starting_obstacle_position = snake.obstacle_pos
        self.starting_obstacle_spawn_counter = snake.obs_spawn_counter
        self.starting_should_obstacle_spawn = snake.obstacle_spawn
        self.starting_direction = snake.direction
        self.starting_new_direction = snake.new_direction
        self.starting_snake_position = snake.snake_pos
        self.starting_snake_body = snake.snake_body
        self.starting_score = snake.score

    def setUp(self):
        """
        Reset global values
        """
        snake.food_pos = self.starting_food_pos
        snake.food_spawn = self.starting_food_spawn
        snake.food_spawn_counter = self.starting_food_spawn_counter
        snake.obstacle_pos = self.starting_obstacle_position
        snake.obs_spawn_counter = self.starting_obstacle_spawn_counter
        snake.obstacle_spawn = self.starting_should_obstacle_spawn
        snake.direction = self.starting_direction
        snake.new_direction = self.starting_new_direction
        snake.snake_pos = self.starting_snake_position
        snake.snake_body = self.starting_snake_body
        snake.score = self.starting_score

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
        """
        pass

    def test_update_snake_position(self):
        """
        """
        pass

    def test_snake_out_of_bounds(self):
        """
        """
        pass

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

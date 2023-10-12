import unittest
from snake.globals import *


class TestSnake(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestSnake, self).__init__(*args, **kwargs)
        self.starting_direction = direction
        self.starting_new_direction = new_direction
        self.starting_snake_position = snake_pos
        self.starting_snake_body = snake_body

    def setUp(self):
        global direction
        global new_direction
        global snake_pos
        global snake_body

        direction = self.starting_direction
        new_direction = self.starting_new_direction
        snake_pos = self.starting_snake_position
        snake_body = self.starting_snake_body

    def test_init_colors(self):
        black, white, red, green, blue = init_colors()

        self.assertEqual(black, pygame.Color(0, 0, 0))
        self.assertEqual(white, pygame.Color(255, 255, 255))
        self.assertEqual(red, pygame.Color(255, 0, 0))
        self.assertEqual(green, pygame.Color(0, 255, 0))
        self.assertEqual(blue, pygame.Color(0, 0, 255))

    def test_init_framesize(self):
        frame_size_x, frame_size_y = init_framesize()

        self.assertEqual(frame_size_x, 720)
        self.assertEqual(frame_size_y, 480)

    def test_init_fps_controller(self):
        fps_controller = init_fps_controller()

        self.assertIsInstance(fps_controller, pygame.time.Clock)

    # TODO: Consider making these functions take parameters instead of globals for more modularised testing (setting globals works but ugly)
    # Testing the function update_snake_position()
    def test_move_right(self):
        pass

    def test_move_left(self):
        pass

    def test_move_up(self):
        pass

    def test_move_down(self):
        pass

    # Testing the function legal_direction()
    def test_legal_direction_up_then_right(self):
        pass

    def test_legal_direction_up_then_left(self):
        pass

    def test_legal_direction_up_then_up(self):
        pass

    def test_legal_direction_up_then_down(self):
        pass

    def test_legal_direction_down_then_right(self):
        pass

    def test_legal_direction_down_then_left(self):
        pass

    def test_legal_direction_down_then_up(self):
        pass

    def test_legal_direction_down_then_down(self):
        pass

    def test_legal_direction_right_then_right(self):
        pass

    def test_legal_direction_right_then_left(self):
        pass

    def test_legal_direction_right_then_up(self):
        pass

    def test_legal_direction_right_then_down(self):
        pass

    def test_legal_direction_left_then_right(self):
        pass

    def test_legal_direction_left_then_left(self):
        pass

    def test_legal_direction_left_then_up(self):
        pass

    def test_legal_direction_left_then_down(self):
        pass


if __name__ == '__main__':
    unittest.main()

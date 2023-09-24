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
        

    #TODO: Consider making these functions take parameters instead of globals for more modularised testing (setting globals works but ugly)
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
from marsrover import MarsRover
import unittest


class TestRover(unittest.TestCase):

    def test_process_command(self):
        rover = MarsRover(Point(3, 3), Direction.E, Point(5, 5))
        rover.process_command('MMRMMRMRRM')

        self.assertEqual(5, rover.pos.cord_x)
        self.assertEqual(1, rover.pos.cord_y)
        self.assertEqual(Direction.E, rover.direction)


if __name__ == '__main__':
    unittest.main()

from enum import Enum


class Point(object):
    cord_x = 0
    cord_y = 0

    def __init__(self, x, y) -> None:
        self.cord_x = x
        self.cord_y = y

    def __str__(self) -> str:
        return "x: {}, y: {}".format(self.cord_x, self.cord_y)


class Direction(Enum):
    N = 0
    S = 2
    E = 3
    W = 1
    lenght = 4


class MarsRover(object):
    pos = Point(0, 0)
    plateau = Point(0, 0)
    direction = Direction.N

    def __init__(self, p: Point, d: Direction, pl: Point) -> None:
        self.pos = p
        self.direction = d
        self.plateau = pl

    def spin_left(self) -> None:
        print('left')
        new_direction = (self.direction.value + 1) % Direction.lenght.value
        self.direction = Direction(new_direction)

    def spin_right(self) -> None:
        print('right')
        new_direction = (self.direction.value - 1)
        if new_direction < 0:
            new_direction = Direction.lenght.value - 1
        self.direction = Direction(new_direction)

    def move_rover(self) -> None:
        if self.direction == Direction.N:
            self.pos.cord_y = self.pos.cord_y + 1

        if self.direction == Direction.S:
            self.pos.cord_y = self.pos.cord_y - 1

        if self.direction == Direction.E:
            self.pos.cord_x = self.pos.cord_x + 1

        if self.direction == Direction.W:
            self.pos.cord_x = self.pos.cord_x - 1

        if self.pos.cord_x > self.plateau.cord_x or self.pos.cord_y > self.plateau.cord_y:
            raise Exception("invalid move")

        print('move rover')

    def process_command(self, command_string: str):
        moves = list(command_string)
        for move in moves:
            if move == 'L':
                self.spin_left()
                print(self.direction)
            elif move == 'R':
                self.spin_right()
                print(self.direction)
            elif move == 'M':
                try:
                    self.move_rover()
                    print(self.pos)
                except Exception as e:
                    raise e
            print('-------')



rover = MarsRover(Point(3, 3), Direction.E, Point(5, 5))
rover.process_command("MMRMMRMRRM")
print(rover.pos)
print(rover.direction)

from coordinate import Coordinate
from board import Board
class Ship:
    
    RIGHT = 0
    DOWN = 1
    UNDEFINED = -1

    def __init__(self, initial_x, initial_y, direction, name, display_char, size, board) -> None:
        #self.coordinates = coordinates
        #self.direction = direction
        self.name = name
        self.size = size
        self.display_char = display_char
        self.coordinate_list = []
        self.board = board
        self.hits = 0
        if direction == Ship.RIGHT:
            if initial_y + self.size > board.width:
                raise Exception("Ship not in bounds")
        elif direction == Ship.DOWN:
            if initial_x + self.size > board.height:
                raise Exception("Ship not in bounds")
        else:
            raise Exception("Invalid ship direction")
        for i in range(0, size):
            if direction == Ship.RIGHT:
                coordinate = self.board.board[initial_x][initial_y + i]
                if coordinate.ship != None:
                    raise Exception("Ship already placed there")
                coordinate.ship = self
            else:
                coordinate = self.board.board[initial_x + i][initial_y]
                if coordinate.ship != None:
                    raise Exception("Ship already placed there")
                coordinate.ship = self

    def is_sunk(self) -> bool:
        return self.hits == self.size

    def register_hit(self):
        self.hits += 1
        return self.is_sunk()
            


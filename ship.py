from coordinate import Coordinate

class Ship:
    
    RIGHT = 0
    DOWN = 1
    UNDEFINED = -1

    def __init__(self, coordinates: Coordinate, direction, name, display_char, size) -> None:
        self.coordinates = coordinates
        self.direction = direction
        self.name = name
        self.size = size
        self.display_char = display_char
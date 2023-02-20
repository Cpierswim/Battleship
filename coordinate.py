class Coordinate:

    STATUS_HIT = 1
    STATUS_MISS = 2
    STATUS_BLANK = 3

    def __init__(self, x, y, board) -> None:
        self.x = x
        self.y = y
        self.ship = None
        self.status = Coordinate.STATUS_BLANK
        self.board = board

    def __str__(self) -> str:
        if self.status == Coordinate.STATUS_BLANK:
            return "-"
        elif self.status == Coordinate.STATUS_HIT:
            return "X"
        elif self.status == Coordinate.STATUS_MISS:
            return "m"
        else:
            raise Exception("Invalid Status Type")
    
    def get_new_Coordinate_from_string(string: str):
        parts = string.split(",", 2)
        test = Coordinate(int(parts[0]), int(parts[1]), None)
        return test
    
    def coordinates_equal(coordinate_one, coordinate_two):
        return coordinate_one.x == coordinate_two.x and coordinate_one.y == coordinate_two.y


    

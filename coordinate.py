class Coordinate:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def create_coordinate_with_XY_Display(input: str):
        coordinate_list = input.split(",", 1)
        x = ord(coordinate_list[0].upper()) - 64 - 1
        y = int(coordinate_list[1]) - 1
        return Coordinate(x, y)
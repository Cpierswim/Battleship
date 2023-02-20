from board import Board
from coordinate import Coordinate
from ship import Ship
from helper import Helper

class Player:
    def __init__(self, name, board_height, board_width) -> None:
        self.name = name
        self.board = Board(board_height, board_width)
        self.unassigned_ships = []
        self.unassigned_ships.append(["Aircraft Carrier", "A", 5])
        self.unassigned_ships.append(["Battleship", "B", 4])
        self.unassigned_ships.append(["Cruiser", "C", 3])
        self.unassigned_ships.append(["Submarine", "S", 3])
        self.unassigned_ships.append(["Destroyer", "D", 2])
        self.ships = []

    def display_board_without_coordinates(self, board_display_names_status):
        self.board.display_board_without_coordinates(board_display_names_status)

    def place_unassigned_ships(self):
        for unassigned_ship in self.unassigned_ships:
            #print("\n\n\n\n\n\n\n\n\n\n\n\n")
            Helper.clearscreen()
            self.display_board_without_coordinates(Board.DISPLAY_SHIP_CHARS_YES)
            print(f"{self.name}: Placing {unassigned_ship[0]} (Size: {unassigned_ship[2]})")
            valid_coordinate_found = False
            while not valid_coordinate_found:
                try:

                    #Get first coordinate of ship and make sure it's inbounds
                    input_inbouds = False
                    input_coordinate = None
                    while not input_inbouds:
                        input_string = input("Place Coordinates (x, y): ")
                        input_coordinate = Coordinate.get_new_Coordinate_from_string(input_string)
                        input_inbouds = self.board.is_inbounds(input_coordinate)
                        if not input_inbouds:
                            print("Input out of bounds, try again")

                    #Get direction of ship
                    direction_valid = False
                    direction = None
                    while not direction_valid:
                        input_string = input("Direction (Right / Down): ")
                        input_string = input_string.lower()
                        if input_string == 'r' or input_string == "right":
                            direction_valid = True
                            direction = Ship.RIGHT
                            pass
                        elif input_string == 'd' or input_string == "down":
                            direction_valid = True
                            direction = Ship.DOWN
                            pass
                        if not direction_valid:
                            print("Input unrecognized")
                    
                    ship = Ship(input_coordinate.x, input_coordinate.y, direction, unassigned_ship[0], unassigned_ship[1], unassigned_ship[2], self.board)
                    valid_coordinate_found = True
                    self.ships.append(ship)
                except:
                    print("Ship cannot be placed there")
        self.unassigned_ships = []
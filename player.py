from board import Board
from coordinate import Coordinate
from ship import Ship
from helper import Helper

class Player:
    def __init__(self, name, board_height, board_width) -> None:
        self.name = name
        self.board = Board(board_height, board_width, self)
        self.unassigned_ships = []
        self.unassigned_ships.append(["Aircraft Carrier", "A", 5])
        self.unassigned_ships.append(["Battleship", "B", 4])
        self.unassigned_ships.append(["Cruiser", "C", 3])
        self.unassigned_ships.append(["Submarine", "S", 3])
        self.unassigned_ships.append(["Destroyer", "D", 2])
        self.ships = []
        self.playing = None

    def display_board_without_coordinates(self, board_display_names_status):
        self.board.display_board_without_coordinates(board_display_names_status)

    def display_board_with_coordinates(self, board_display_names_status):
        self.board.display_board_with_coordinates(board_display_names_status)

    def place_unassigned_ships(self):
        for unassigned_ship in self.unassigned_ships:
            #print("\n\n\n\n\n\n\n\n\n\n\n\n")
            Helper.clearscreen()
            self.display_board_with_coordinates(Board.DISPLAY_SHIP_CHARS_YES)
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
                    
                    # TODO: Make sure the ship can be placed there - 
                    if self.can_ship_be_placed_there(input_coordinate, direction, unassigned_ship[2]):
                        ship = Ship(input_coordinate.x, input_coordinate.y, direction, unassigned_ship[0], unassigned_ship[1], unassigned_ship[2], self.board)
                        valid_coordinate_found = True
                        self.ships.append(ship)
                    else:
                        raise Exception("Cannot be placed there")
                except TypeError:
                    print("Input not understood")
                except:
                    print("Ship cannot be placed there")
        self.unassigned_ships = []

    def can_ship_be_placed_there(self, initial_coordinate, direction, size) -> bool:
        for i in range(0, size):
            coordinate = None
            if direction == Ship.RIGHT:
                coordinate = self.board.get_coordinate_at(initial_coordinate.x, initial_coordinate.y + i)
            elif direction == Ship.DOWN:
                coordinate = self.board.get_coordinate_at(initial_coordinate.x + i, initial_coordinate.y) 
            else:
                raise Exception()
            if not coordinate.ship == None:
                return False
        return True

    def is_all_ships_sunk(self):
        for ship in self.ships:
            if not ship.is_sunk():
                return False
        return True

    def get_current_score(self) -> int:
        score = 0
        for ship in self.ships:
            if ship.is_sunk():
                score += 1
        return score

    def take_turn(self):
        Helper.clearscreen()
        print("Where they have played against your boats:")
        self.board.display_board_with_coordinates(Board.DISPLAY_SHIP_CHARS_YES)
        print(f"\n\nCurrent Score\n{self.name}: {self.playing.get_current_score()}\n{self.playing.name}: {self.get_current_score()}")
        print(f"\n\nPlaying: {self.name}\n\n")
        self.playing.display_board_with_coordinates(Board.DISPLAY_SHIP_CHARS_NO)
        valid_coordinate = False
        coordinate_in_bounds = False
        board_coordinate = None
        move_made = False
        while not move_made: #This exists so that if I want to recode to allow a re-entry of coordinates if they match a hit or miss
            while not valid_coordinate or not coordinate_in_bounds:
                try:
                    coordinate_as_string = input("\nWhere to play (x, y): ")
                    entered_coordinate = Coordinate.get_new_Coordinate_from_string(coordinate_as_string)
                    valid_coordinate = True
                except:
                    print("Coordinate not recognized, please type in format such as: A, 4")
                try:
                    board_coordinate = self.playing.board.get_coordinate_at(entered_coordinate.x, entered_coordinate.y) 
                    coordinate_in_bounds = True
                except:
                    print("Coordinate out of bounds. Try again")
            if board_coordinate.status == Coordinate.STATUS_BLANK:
                if board_coordinate.ship == None:
                    board_coordinate.status = Coordinate.STATUS_MISS
                    move_made = True
                    print("\n\n - miss")                    
                else:
                    board_coordinate.status = Coordinate.STATUS_HIT
                    ship_sunk = board_coordinate.ship.register_hit()
                    move_made = True
                    print("\n\nHIT!!!!!     You have registered a hit!")
                    if ship_sunk:
                        print(f"You sunk their {board_coordinate.ship.name}")
            elif board_coordinate.status == Coordinate.STATUS_MISS:
                move_made = True
                print("\n\nWhoops - you already played there. You'll miss this turn")
            elif board_coordinate.status == Coordinate.STATUS_HIT:
                move_made = True
                print("\n\nWhoops - You already made a hit there. You'll miss this turn")


        input("\n\nPress Enter to clear the screen")
        



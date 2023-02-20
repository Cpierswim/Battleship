from ship import Ship
from coordinate import Coordinate

class PlayerArea:
    def __init__(self, width, height) -> None:
        self.board = self.create_board(width, height)
        self.ship_list = []
        self.ship_list.append(Ship(Coordinate(-1, -1), Ship.UNDEFINED, "Aircraft Carrier", "A", 5))
        self.ship_list.append(Ship(Coordinate(-1, -1), Ship.UNDEFINED, "Battleship", 'B', 4))
        self.ship_list.append(Ship(Coordinate(-1, -1), Ship.UNDEFINED, "Cruiser", 'C', 3))
        self.ship_list.append(Ship(Coordinate(-1, -1), Ship.UNDEFINED, "Submarine", 'S', 3))
        self.ship_list.append(Ship(Coordinate(-1, -1), Ship.UNDEFINED, "Destroyer", 'D', 2))
        
    def max_y_colums(self) -> int:
        return len(self.board[0])
    
    def max_x_rows(self) -> int:
        return len(self.board)

    def create_board(self, width, height):
        board = []
        for i in range(0, height):
            line = []
            for j in range(0, width):
                line.append('-')
            board.append(line)
        return board

    def print_board(self):
        display_board = []
        
        y_display = []
        for i in range(0, len(self.board[0])):
            y_display.append(str(i + 1))
        display_board.append(y_display)
        for line in self.board:
            display_board.append(line.copy())
        
        for ship in self.ship_list:
            if ship.direction != Ship.UNDEFINED:
                for i in range(0, ship.size):
                    if ship.direction == Ship.RIGHT:
                        display_board[ship.coordinates.x + 1][ship.coordinates.y + i] = ship.display_char
                    elif ship.direction == Ship.DOWN:
                        display_board[ship.coordinates.x + 1 + i][ship.coordinates.y] = ship.display_char

        for i in range(0, len(display_board)):
            if i == 0:
                print(" ", display_board[i])
            else:
                print(chr(i + 64), display_board[i])
        
    def clear_screen():
        print("\n\n\n\n\n\n\n\n\n")

    def place_ships(self):
        for ship in self.ship_list:
            if ship.direction == Ship.UNDEFINED:
                coordinates_received = False
                PlayerArea.clear_screen()
                self.print_board()
                print(f"Placing {ship.name} ({ship.size} spaces):")
                while not coordinates_received:
                    try:
                        coordinates_input_as_string = input("X, Y Coordinates: ")
                        input_coordinates = Coordinate.create_coordinate_with_XY_Display(coordinates_input_as_string)
                        if input_coordinates.y <= self.max_y_colums() and input_coordinates.y > -1 and input_coordinates.x > -1 and input_coordinates.x <= self.max_x_rows(): 
                            coordinates_received = True 
                            ship.coordinates = input_coordinates
                        else:
                            raise Exception("Invalid coordinates")
                    except:
                        print("Invalid Coordinates, please select again")
                direction_receieved = False
                while not direction_receieved:
                    direction_input = input("To the right or down: ")
                    direction_input = direction_input.lower()
                    if(direction_input == "right" or direction_input == "r"):
                        ship.direction = Ship.RIGHT
                        direction_receieved = True
                    elif direction_input == "down" or direction_input == "d":
                        ship.direction = Ship.DOWN
                        direction_receieved = True
                    else:
                        print("Invalid direction, please select again")

                        



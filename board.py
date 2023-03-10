from coordinate import Coordinate

class Board:

    DISPLAY_SHIP_CHARS_YES = 1
    DISPLAY_SHIP_CHARS_NO = 2

    def __init__(self, height, width, player) -> None:
        self.board = []
        self.height = height
        self.width = width
        self.player = player
        for x in range(0, height):
            line = []
            for y in range(0, width):
                line.append(Coordinate(x, y, self))
            self.board.append(line)

    def get_coordinate_at(self, x, y):
        return self.board[x][y]

    def is_inbounds(self, coordinate) -> bool:
        try:
            test = self.board[coordinate.x][coordinate.y]
            return True
        except:
            return False

    def clear_display():
        print("\n\n\n\n\n\n\n\n\n")

    def display_board_without_coordinates(self, display_names_status):
        if display_names_status != Board.DISPLAY_SHIP_CHARS_YES:
            display_names_status = Board.DISPLAY_SHIP_CHARS_NO
        display = []
        for x in range(0, self.height):
            line = []
            for y in range(0, self.width):
                if self.board[x][y].status == Coordinate.STATUS_BLANK:
                    if self.board[x][y].ship == None or display_names_status == Board.DISPLAY_SHIP_CHARS_NO:
                        line.append("-")
                    else:
                        line.append(self.board[x][y].ship.display_char)
                elif self.board[x][y].status == Coordinate.STATUS_HIT:
                    line.append("X")
                else:
                    line.append("m")
            display.append(line)


        for line in display:
            print(line)

    def display_board_with_coordinates(self, display_names_status):
        if display_names_status != Board.DISPLAY_SHIP_CHARS_YES:
            display_names_status = Board.DISPLAY_SHIP_CHARS_NO
        display = []
        first_line = []
        first_line.append(" ")
        for i in range(0, self.width):
            first_line.append(str(i + 1))
        display.append(first_line)
        for x in range(0, self.height):
            line = []
            line.append(chr(x + 65))
            for y in range(0, self.width):
                if self.board[x][y].status == Coordinate.STATUS_BLANK:
                    if self.board[x][y].ship == None or display_names_status == Board.DISPLAY_SHIP_CHARS_NO:
                        line.append("-")
                    else:
                        line.append(self.board[x][y].ship.display_char)
                elif self.board[x][y].status == Coordinate.STATUS_HIT:
                    line.append("X")
                else:
                    line.append("m")
            display.append(line)

        for line in display:
            print(line)
                    
    
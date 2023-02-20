from player import Player

class Game:

    STANDARD_BOARD_HEIGHT = 10
    STANDARD_BOARD_WIDTH = 10

    def __init__(self) -> None:
        self.player_list = []

    def create_players(number_to_create):
        for i in range(0, number_to_create + 1):
            player = Player("Player" + str(i), Game.STANDARD_BOARD_HEIGHT, Game.STANDARD_BOARD_WIDTH)

    def place_ships(self):
        for player in self.player_list:
            player.place_unassigned_ships()
from player import Player
from helper import Helper
import time

class Game:

    STANDARD_BOARD_HEIGHT = 10
    STANDARD_BOARD_WIDTH = 10

    def __init__(self) -> None:
        self.player_list = []

    def create_players(self, number_to_create):
        Helper.clearscreen()
        print(f"Creating {number_to_create} players")
        time.sleep(2)
        for i in range(0, number_to_create + 1):
            player = Player("Player" + str(i + 1), Game.STANDARD_BOARD_HEIGHT, Game.STANDARD_BOARD_WIDTH)
            self.player_list.append(player)

    def place_ships(self):
        for player in self.player_list:
            player.place_unassigned_ships()
            Helper.clearscreen()
            print(f"{player.name} is finished placing their ships")
            input("Input anything to continue to the next player: ")

    
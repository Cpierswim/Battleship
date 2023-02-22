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
        player_to_create_list = []
        for i in range(1, number_to_create + 1):
            name_added = False
            while not name_added:
                name = input(f"Name for player {i}: ")
                name = name.strip()
                if name == "":
                    print("Name cannot be empty")
                else:
                    name_added = True
            player_to_create_list.append(name)
        for i in range(0, number_to_create):
            player = Player(player_to_create_list[i], Game.STANDARD_BOARD_HEIGHT, Game.STANDARD_BOARD_WIDTH)
            self.player_list.append(player)
        
        #right now, you can only play with 2, but up to this point, everything is set up so you could figure out a way to play with more than 2
        self.player_list[0].playing = self.player_list[1]
        self.player_list[1].playing = self.player_list[0]

    def place_ships(self):
        for player in self.player_list:
            player.place_unassigned_ships()
            Helper.clearscreen()
            print(f"{player.name} is finished placing their ships")
            input("Input anything to continue to the next player: ")

    def temp_place_ships(self):
        for player in self.player_list:
            player.temp_placeships()

    def is_any_player_dead(self):
        for player in self.player_list:
            if player.is_all_ships_sunk():
                return True
        return False

    def play(self):
        while not self.is_any_player_dead():
            player = self.player_list[0]
            Game.perform_player_switch()
            player.take_turn()
            if not self.is_any_player_dead():
                player = self.player_list[1]
                Game.perform_player_switch()
                player.take_turn()
        
        if self.player_list[0].is_all_ships_sunk():
            Helper.clearscreen()
            print(f"Congradulations {self.player_list[1].name}, you WIN!")
        elif self.player_list[1].is_all_ships_sunk():
            Helper.clearscreen()
            print(f"Congradulations {self.player_list[0].name}, you WIN!")
        else:
            print("Something is wrong")


    def perform_player_switch():
        Helper.clearscreen()
        input("Press enter when you have switched players")
        Helper.clearscreen()

    
from game import Game

game = Game()

game.create_players(2)
game.place_ships()
#game.temp_place_ships()
game.play()



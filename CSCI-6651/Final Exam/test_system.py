from Riddhi_Sanghvi_Final_Exam import Game, ShipType

#test for checking the game flow 
def test_complete_game():
    game = Game("Riddhi", "Vidhi")                      #Creating new instance for the 2 players 

    st = ShipType("Destroyer", 3, 1)                    # define a single destroyer ship of length 3 

    game.players[0].board.place_ship(st, 2, 2, 'H')     #placing the ship horizontally for player 1

    game.players[1].board.place_ship(st, 5,5 ,'H')      #placing it vertically for player 2

    guesses = [(5,4),(5,5),(5,6)]                       #Player 1 guesses all the cell of the Player 2 's destroyer
    for r, c in guesses:
        result, sunk = game.make_guess(r,c)

    assert game.is_over() is True                       #after all the cell are of the ships are hit the game is over
    assert game.winner().name == "Riddhi"               #Player 1 should be the winner
    
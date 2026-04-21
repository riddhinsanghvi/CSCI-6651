from Riddhi_Sanghvi_Final_Exam import Game, ShipType

#Small function to set up a game for each player
def setup_game():
    game = Game("Riddhi", "Vidhi")

    st = ShipType("Destroyer", 3, 1)
    game.players[0].board.place_ship(st, 5, 5, 'H')
    game.players[1].board.place_ship(st, 7,7,'H')

    return game

# test to check if the guessing of a hit is registered correctly
def test_game_hit():
    game = setup_game()

    r, c = 7, 7
    result, sunk = game.make_guess(r,c)
    
    assert result == "HIT"
    assert sunk is None

# test to check if the guessing of a Dhip sunk is registered correctly
def test_game_ship_sunk():
    game = setup_game
    for column in [6,7,8]:
        r, c = 7, column
        result, sunk = game.make_guess(r,c)

    assert result == "SHIP SUNK"
    assert sunk == "Destroyer"

#Test to see if switching turn is working as required
def test_turn_switching():
    game = setup_game()

    first = game.get_active_player().name
    game.switch_turn()
    second = game.get_active_player().name

    assert first!=second
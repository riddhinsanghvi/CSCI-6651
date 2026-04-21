from Riddhi_Sanghvi_Final_Exam import Board, ShipType

#test to check if the ship is placed correctly within the board bound
def test_valid_ship_placement():
    board = Board()
    st = ShipType("Destroyer", 3, 1)

    ok, message = board.can_place_ship(st, 5,5,'H')
    assert ok is True

#test to check if the ship is placed outside of the board and if it rejected
def test_out_of_bound_reject():
    board = Board()
    st = ShipType("Carrier",9,1)

    ok, message = board.can_place_ship(st, 0,0,'H')
    assert ok is False

#test to check overlapping of ships is not allowed
def test_ship_collision_reject():
    board = Board()
    st = ShipType("Destroyer", 3, 1)

    board.place_ship(st, 5,5,'H')
    ok, message = board.can_place_ship(st, 5,5,'V')
    assert ok is False

#test to check if the ship lookup works correctly
def test_ship_lookup():
    board = Board()
    st = ShipType("Destroyer", 3, 1)

    ship = board.place_ship(st, 4,4,'H')

    found = board.ship_at(4,4)
    assert found == ship

#test for placing ship at the top i.e., A,0 with orientation H
def test_top_horizontal_out_of_bound():
    board = Board()
    st = ShipType("Destroyer", 3, 1)

    ok, message = board.can_place_ship(st, 0,0,'H')
    assert ok is False

#test for placing ship at the top i.e., A,0 with orientation V
def test_top_vertical_out_of_bound():
    board = Board()
    st = ShipType("Destroyer", 3, 1)

    ok, message = board.can_place_ship(st, 25, 9,'V')
    assert ok is False
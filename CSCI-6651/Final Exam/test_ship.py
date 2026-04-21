from Riddhi_Sanghvi_Final_Exam import Ship, ShipType

#Test if the horizontal ship generates the correct list of occupied cells
def test_horizontal_ship_cell_generation():
    st = ShipType("Destroyer" , 3,1 )
    ship  = Ship(st, 5, 5,'H')

    result = [(5,4),(5,5),(5,6)]
    assert ship.cells == result

#Test if the vertical ship generates the correct list of occupied cells
def test_vertical_ship_cell_generation():
    st = ShipType("Destroyer", 3,1)
    ship = Ship(st, 5, 5, 'V')

    result = [(4,5),(5,5,),(6,5)]
    assert ship.cells == result

#test registering the hit and check if the ship sunk
def test_ship_hit_and_sunk():
    st = ShipType("Destroyer", 3, 1)
    ship = Ship(st, 5, 5, 'H')

    for cell in ship.cells:
        ship.register_hits(*cell)

    assert ship.is_sunk() is True
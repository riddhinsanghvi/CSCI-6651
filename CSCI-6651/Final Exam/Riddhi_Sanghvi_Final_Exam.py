import json
import os
import datetime
from typing import List, Tuple, Dict, Optional

#Board dimensions 
ROWS = 26
COLUMNS = 10
ROW_LETTERS = [chr(ord('A')+i) for i in range(ROWS)]
RECORDS_FILE = "battleship_records.json"                #file to same the game records

#Class representing the Ship types in the game
class ShipType:
    def __init__(self, name:str, length:int, count:int):
        self.name = name                                #Name of the ship
        self.length = length                            #number of cell required to occupy that ship
        self.count = count                              # Number of ships on the board of that particular type

#Predefined ship types
SHIP_TYPES = [
    ShipType("Destroyer", 3, 2),
    ShipType("Cruiser", 5, 1),
    ShipType("Batttleship", 7,1),
    ShipType("Aircraft Carrier",9,1)
]

#Convert the coordinate tuple to number indices
def coord_to_index(coord: Tuple[str, int]) -> Tuple[int,int ]:
    row_letter, column = coord
    r = ord(row_letter.upper())-ord('A')
    c = int(column)
    return r, c

#convert number indices to coordinate tuple
def index_to_coord(r:int, c: int) -> Tuple[str, int]:
    return ROW_LETTERS[r], c

#Class representing an individual ship on the board 
class Ship:

    def __init__(self, ship_type: ShipType, mid_row:int, mid_column:int, orientation:str):
        self.type = ship_type
        self.length = ship_type.length
        self.orientation = orientation.upper()
        self.mid = (mid_row, mid_column)                #middle coordinates of the ship
        self.cells = self.compute_cells()               #list of all the cells the ships occupy
        self.hits = set()                               #track the hits on the ship

    #Compute the cells occupied by the ship based on the orientation
    def compute_cells(self) -> List[Tuple[int, int]]:
        half = self.length //2
        r_mid, c_mid = self.mid
        cells = []
        for offset in range(-half, half+1):
            if self.orientation == 'H':                 #For horizontal orientation
                r = r_mid
                c = c_mid + offset
            else:                                       #For vertical orientation
                r = r_mid + offset
                c = c_mid
            cells.append((r,c))
        return cells
    
    #Check if a ship is occupied at the cuurent cell
    def is_at(self, r:int, c:int):
        return (r,c) in self.cells
    
    #mark hit on the ship
    def register_hits(self, r: int, c:int) ->None:
        if self.is_at(r,c):
            self.hits.add((r,c))

    #Check if the ship is completely sunk
    def is_sunk(self) -> bool:
        return len(self.hits) >=self.length
    
    #Check the number of hits remaining for the ship to sink
    def remaining_hits(self) -> int:
        return max(0, self.length - len(self.hits))
    
#representing the players board
class Board:
    def __init__(self):
        self.ships: List[Ship] = []                                 #List of ships on the board
        self.occupancy: Dict[Tuple[int,int], Ship] = {}             #Map of cell and ship

    #check if a ship can be placed at a position
    def can_place_ship(self, ship_type:ShipType, mid_r:int, mid_c:int, orientation:str)->Tuple[bool, Optional[str]]:
        orientation = orientation.upper()
        if orientation not in ('H','V'):
            return False, "Orientation must be 'H' or 'V' "
        half = ship_type.length // 2

        for offset in range(-half, half+1):
            r = mid_r + (0 if orientation =='H' else offset)
            c = mid_c +(offset if orientation =='H' else 0)
            if r<0 or r>=ROWS or c<0 or c>=COLUMNS:
                return False, f"{ship_type.name} would be out of board bounds "
            if (r, c) in self.occupancy:
                return False, f"Position collides with another ship at {index_to_coord(r, c)}"
        return True, None
    
    #place a ship on the board
    def place_ship(self, ship_type: ShipType, mid_r:int, mid_c: int, orientation:str) ->Ship:
        ship = Ship(ship_type, mid_r, mid_c, orientation)
        self.ships.append(ship)
        for cell in ship.cells:
            self.occupancy[cell] = ship
        return ship
        
    #remove all the ships from the board
    def remove_all_ships(self) ->None:
        self.ships = []
        self.occupancy = {}

    #Remove particular ship from the board
    def remove_ship(self, ship:Ship) ->None:
        if ship in self.ships:
            self.ships.remove(ship)
            for cell in ship.cells:
                self.occupancy.pop(cell, None)
    
    #Check if all the ships on the board are sunk
    def all_sunk(self)->bool:
        return all(ship.is_sunk() for ship in self.ships)
    
    # chekc if the ship is at a particular cell
    def ship_at(self, r:int, c:int) -> Optional[Ship]:
        return self.occupancy.get((r,c))
    
#class represnting a particular player
class Player:
    def __init__(self, name:str):
        self.name = name
        self.board = Board()
        #guesses tracked as dict (r,c) -> 'H' or 'M' for hit or Miss
        self.guesses: Dict[Tuple[int, int], str] = {}
        self.guess_count = 0 # number of guesses made by this player during a game

    #Record the guess on the opponenets board
    def record_guess(self, r:int, c:int, result:str):
        self.guesses[(r,c)] = result
        self.guess_count +=1

    #check if the position was guessed before
    def has_guessed(self, r:int, c:int) -> bool:
        return (r, c) in self.guesses

#Class representing the game itself
class Game:
    def __init__(self, p1_name:str, p2_name:str):
        self.players = [Player(p1_name), Player(p2_name)]
        self.active_index = 0
        self.total_turns = 0
    
    #get the active player
    def get_active_player(self) -> Player:
        return self.players[self.active_index]
    
    #Get the other player
    def get_other_player(self) -> Player:
        return self.players[1 - self.active_index]
    
    #method to switch the turn betwween the active player and the other player
    def switch_turn(self):
        self.active_index = 1 - self.active_index
        self.total_turns +=1

    #method to make a guess for each player
    def make_guess(self, r:int, c:int) ->Tuple[str, Optional[str]]:
        ap = self.get_active_player()
        op = self.get_other_player()

        if ap.has_guessed(r, c):
            raise ValueError("Already guessed that position")
        
        ship  = op.board.ship_at(r,c)
        if not ship:
            ap.record_guess(r,c,'M')
            return "MISS", None
        
        #if it is a HIT
        ship.register_hits(r, c)
        ap.record_guess(r,c, 'H')
        if ship.is_sunk():
            return "SHIP SUNK", ship.type.name
        
        else:
            return "HIT", None
    
    #check if the game is over
    def is_over(self) -> bool:
        return any(player.board.all_sunk() for player in self.players)
    
    #Return the winner of the game 
    def winner(self) -> Optional[Player]:
        if not self.is_over():
            return None
        for player in self.players:
            if not player.board.all_sunk():
                return player
        return None


def clear_screen_hint():
    print("\n"+ "-"*50+"\n")

def prompt_secret_pass():
    input("Pass the keyboard to the other player. Press ENTER when ready...")

#displaye the winners guesses on the board
def display_guess_board(player: Player):
    print(f"\n{player.name}'s Guess Board (x = Hit, 0 = Miss, . = unknown)\n")
    header = "   " + " ".join(str(c) for c in range(COLUMNS))

    print(header)
    for r in range(ROWS):
        row_label = ROW_LETTERS[r]
        row_cells = []
        for c in range(COLUMNS):
            ch = '.'
            value = player.guesses.get((r, c))
            if value =='H':
                ch = 'X'
            elif value == 'M':
                ch = '0'
            row_cells.append(ch)
        print(f"{row_label:2} "+" ".join(row_cells))
    print()

#Display player board with all the ships in between placement
def display_player_ship_board_with_ships(player: Player, reveal_unhit_ships:bool = True):
    """
    Display players own board: Show ships(S), hits (X), misses(0) relative to enemy guesses.
    reveal_unhit_ships: if True, show 'S' for ship positions not hit. 
    """
    print(f"\n{player.name}'s Board (X=hit, 0=empty guess by opponent, S = Ship present)\n")
    header = "   " + " ".join(str(c) for c in range(COLUMNS))
    print(header)

    ship_cells = {}
    for ship in player.board.ships:
        for cell in ship.cells:
            ship_cells[cell] = ship

    for r in range(ROWS):
        row_label = ROW_LETTERS[r]
        row_cells = []
        for c in range(COLUMNS):
            ch = '.'
            if (r, c )in ship_cells:
                if ship_cells[(r,c)].is_at(r,c) and (r, c) in ship_cells[(r,c)].hits:
                    ch = 'X'
                else:
                    ch = 'S' if reveal_unhit_ships else '.'
            row_cells.append(ch)
        print(f"{row_label:2} "+" ".join(row_cells))
    print()

#display all the ships on board after the game ends
def display_final_boards(game: Game):
    #Show each player's guess board with S for unhit ships on the opponent
    print("\nFinal Boards\n")
    for idx, player in enumerate(game.players):
        #SHow players guesses against opponent
        opponent = game.players[1-idx]
        print(f"\n{player.name}'s Guess Board (final) - guesses against {opponent.name}")
        header = "   " + " ".join(str(c) for c in range(COLUMNS))
        print(header)
        for r in range(ROWS):
            row_label = ROW_LETTERS[r]
            row_cells = []
            for c in range(COLUMNS):
                if (r, c) in player.guesses:
                    value = player.guesses[(r, c)]
                    row_cells.append('X' if value =='H' else '0')
                else:
                    ship = opponent.board.ship_at(r,c)
                    if ship and (r,c) not in ship.hits:
                        row_cells.append('S')
                    else:
                        row_cells.append('.')
            print(f"{row_label:2} "+ " ".join(row_cells))
    print()

#load the high score records
def load_records():
    if not os.path.exists(RECORDS_FILE):
        return []
    try:
        with open(RECORDS_FILE, 'r')as f:
            return json.load(f)
    except Exception:
        return []
    
#Save the game records in the json file
def save_record(record: dict):
    recs = load_records()
    recs.append(record)
    with open(RECORDS_FILE, 'w') as f:
        json.dump(recs, f, indent = 2, default = str)

#Load the high score statistics from the json file and display them
def show_high_score():
    recs = load_records()
    if not recs:
        print("No high score yet. Be the first to set one!")
        return 
    
    min_guess = min(r.get('winner_guesses', float('inf')) for r in recs)
    top = [r for r in recs if r.get('winner_guesses') == min_guess]
    print(f"Current High Score: {min_guess} guesses. (Recorded {len(top)} time(s))")
    #show recent one
    recent = sorted(recs, key = lambda x: x.get('timestamp',''), reverse=True)[0]
    print(f"Most recent winner: {recent.get('winner_name')} on {recent.get('timestamp')}")

#Function to get the players names
def prompt_player_name(player_number: int)->str:
    while True:
        name = input(f"Enter name for Player {player_number}: ").strip()
        if name:
            return name
        print("name cannot be blank")

#prompt to place at the ships for each player
def prompt_ship_placement_for_player(player: Player):
    print(f"\n{player.name}: place your ships in secret.")
    print("Board rows: A-Z. Columns:0-9")
    print("Ships must be placed by their middle cell ")
    #For each ship type and count
    placement = []
    for st in SHIP_TYPES:
        for i in range(st.count):
            while True:
                print(f"\nPlacing {st.name} (length {st.length}).")
                user_input = input("Enter the middle position as RowLetter, ColumnNumber(e.g., A,1) or show to view the current board: ").strip()
                if user_input.lower() == 'show':
                    #This will show the ship positions on their board(S for ships)
                    display_player_ship_board_with_ships(player, reveal_unhit_ships=True)
                    continue
                parts = [p.strip() for p in user_input.replace(" ","").split(",") if p.strip()]
                if len(parts)!=2:
                    print("Invalid format. Use e.g., A,1")
                    continue
                row_letter, col_str = parts
                if len(row_letter)!=1 or row_letter.upper() not in ROW_LETTERS:
                    print("Invalid row. Must be A-Z")
                    continue
                if not col_str.isdigit() or not (0 <= int(col_str)< COLUMNS):
                    print("INVALID column. Must be 0-9" )
                    continue
                orientation  = input("Orientation H(horizontal) or V (vertical): ").strip().upper()
                if orientation not in ('H','V'):
                    print("Invalid orientation. Enter H or V")
                    continue
                mid_r = ord(row_letter.upper())- ord('A')
                mid_c = int(col_str)
                ok, message = player.board.can_place_ship(st, mid_r, mid_c, orientation)
                if not ok:
                    print("Cannot place ship: ", message)
                    continue
                player.board.place_ship(st, mid_r, mid_c, orientation)
                print(f"{st.name} placed at {row_letter.upper()}, {mid_c} {orientation}")
                break

    #After all placed, show board and ask confirmation/ replacement
    while True:
        print("\nFinal placement for review: ")
        display_player_ship_board_with_ships(player, reveal_unhit_ships=True)
        resp = input("Confirm Placement?(Y = accept, R = Replace a specific ship, A =Replace all the ships): ").strip().upper()
        if resp == 'Y':
            break 
        elif resp == 'A':
            player.board.remove_all_ships()
            print("All ships removed. Re-place ships")
            prompt_ship_placement_for_player(player)
            return
        elif resp == 'R':
            print("Ships on board: ")
            for idx, ship in enumerate(player.board.ships):
                mr, mc = ship.mid
                print(f"{idx}: {ship.type.name} mid {index_to_coord(mr, mc)} orientation {ship.orientation}")
            choice = input("Enter index of the ship to remove, or 'C' to cancel: ").strip()
            if choice.upper() == 'C':
                continue
            if not choice.isdigit() or not (0 <= int(choice) < len(player.board.ships)):
                print("Invalid index")
                continue
            idx = int(choice)
            player.board.remove_ship(player.board.ships[idx])
            print("Removed Ship. Please place replacement for that ship now.")
            #get the new placement for the removed ship type
            st = SHIP_TYPES[0] # placement: we must find the matching type by length
            # find the removed ship tyoe: we can prompt selection
            print("Enter placement for the replacement ship.")
            #prompt exact same process for a ship ship
            while True:
                user_input = input("Enter middle position as RowLetter, ColumnNumber(e.g., A,1) or 'show' to view the current board: ").strip()
                if user_input.lower() == 'show':
                    display_player_ship_board_with_ships(player, reveal_unhit_ships=True)
                    continue

                parts = [p.strip() for p in user_input.replace(" ", "").split(",") if p.strip()]
                if len(parts)!=2:
                    print("INVALID format. Use e.g., A,1")
                    continue
                row_letter, col_str = parts
                if len(row_letter)!=1 or row_letter.upper() not in ROW_LETTERS:
                    print("Invalid row. Must be A-Z")
                    continue
                if not col_str.isdigit() or not (0 <= int(col_str)< COLUMNS):
                    print("INVALID column. Must be 0-9" )
                    continue
                orientation  = input("Orientation H(horizontal) or V (vertical): ").strip().upper()
                if orientation not in ('H','V'):
                    print("Invalid orientation. Enter H or V")
                    continue
                mid_r = ord(row_letter.upper())- ord('A')
                mid_c = int(col_str)
                # Need ship length for the replacement: ask user for the length/ name
                print("Which ship are you replacing? Options:")
                for j, stt in enumerate(SHIP_TYPES):
                    print(f"{j}: {stt.name} (length {stt.length})")
                idx_st = input("Enter index of the ship type: ")
                if not idx_st.isdigit() or not (0<= int(idx_st)< len(SHIP_TYPES)):
                    print("INVALID ship type index")
                    continue
                st = SHIP_TYPES[int(idx_st)]
                ok, message  = player.board.can_place_ship(st, mid_r, mid_c, orientation)
                if not ok:
                    print("Cannot place ship: ", message)
                    continue
                player.board.place_ship(st, mid_r, mid_c, orientation)
                print(f"{st.name} placed at {row_letter.upper()}, {mid_c} {orientation}")
                break
            #after replace, loop back to confirm
        else:
            print("Enter Y, R or A: ")

#convert the user input in grid index
def parse_guess_input(s:str ) -> Tuple[int, int ]:
    s_clean = s.replace(" ", "").replace(",","")
    if len(s_clean)<2:
        raise ValueError("Invalid Guess Format ")
    row_letter = s_clean[0].upper()
    col_str = s_clean[1:]
    if row_letter not in ROW_LETTERS:
        raise ValueError("Row must be A-Z")
    if not col_str.isdigit() or not (0<= int(col_str)< COLUMNS):
        raise ValueError("Column must be 0-9")
    r = ord(row_letter) - ord('A')
    c = int(col_str)
    return r, c

#Main game 
def play_game():
    print("-"*50)
    print("Welcome to Battleship!")
    print("-"*50)
    show_high_score()
    p1 = prompt_player_name(1)
    p2 = prompt_player_name(2)
    game = Game(p1, p2)

    #Place the ships for both the players, secretively
    for idx, player in enumerate(game.players):
        clear_screen_hint()
        print(f"{player.name}: prepare to place the ships")
        prompt_secret_pass()
        prompt_ship_placement_for_player(player)
        clear_screen_hint()
        print(f"{player.name}, your placement has been recorded.")
        prompt_secret_pass()

    #Confirm Start
    while True:
        resp = input("Begin play?(Y/N): ").strip().upper()
        if resp == 'Y':
            break
        elif resp == 'N':
            print("Exiting")
            return
        else:
            print("Enter Y or N: ")
    
    #Play Loop
    game.active_index = 0 #player 1 starts
    while not game.is_over():
        ap = game.get_active_player()
        op = game.get_other_player()

        clear_screen_hint()
        print(f"Turn for {ap.name} ")
        display_guess_board(ap)
        #Prompt Guess
        while True:
            guess_input = input(f"{ap.name}, enter your guess as Row, Column(e.g., A,1): ").strip()
            try:
                r, c = parse_guess_input(guess_input)
            except ValueError as v:
                print("Input Error: ", v)
                continue
            if ap.has_guessed(r, c):
                print("You already guessed that coordinate. Try another. ")
                continue
            #perform guess
            try:
                result, sunk_ship_name = game.make_guess(r, c)
            except ValueError as e:
                print("Error: ", e )
                continue
            if result == "MISS":
                print("MISS")
            elif result == "HIT":
                print("HIT")
            elif result == "SHIP SUNK":
                print(f"SHIP SUNK! {sunk_ship_name}")
            break
        #After gues, check game over
        if game.is_over():
            break
        #Switch turn 
        game.switch_turn()
        prompt_secret_pass()

    
    #Game Over
    clear_screen_hint()
    winner = game.winner()
    if winner:
        loser = game.players[1] if game.players[0] is winner else game.players[0]
        print(f"Game over. Winner: {winner.name}")
        #numer of guesses by winner
        winner_guesses = winner.guess_count
        remaining_ships = sum(1 for s in winner.board.ships if not s.is_sunk())
        print(f"Winner guesses: {winner_guesses}. Remaining ships for winner: {remaining_ships}")
        #display final boards
        display_final_boards(game)
        #save records
        records = {
            "timestamp": datetime.datetime.now().isoformat(),
            "winner_name": winner.name,
            "winner_guesses":winner_guesses,
            "remianing_ships": remaining_ships,
            "total_turns": game.total_turns+1,
            "players": [p.name for p in game.players]
        }
        save_record(records)
        print("Game record saved.")
    else:
        print("Game ended with no winner(unexpected)")


if __name__ == "__main__":
    play_game()
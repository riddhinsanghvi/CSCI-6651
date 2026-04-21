class PlayerTurn:
    def get_guess(self):#
        #Take the input from the user
        raw = input("\n Enter a letter or full word(or Type EXIT to End): ").strip()
        if raw.lower() == "exit": #check if the player wants to exit the game
            return None
        return raw
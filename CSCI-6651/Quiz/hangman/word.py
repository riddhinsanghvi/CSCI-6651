class HangmanWord:
    def __init__(self, text):
        self.original = text.lower()
        self.revealed = ["_" if c.isalpha() else c for c in self.original]

    def reveal_letter(self, letter):
        #Reveals all occurrences of a guessed letter in the word
        found = False

        for i, ch in enumerate(self.original):
            if ch == letter:
                self.revealed[i]= ch
                found = True
        return found
    
    def reveal_full(self):
        #Reveals the entire word/phrase
        self.revealed = list(self.original)

    def is_fully_revealed(self):
        #checks if all letters in the word have been revealed
        return "_" not in self.revealed
    
    def display(self):
        #returns a string representation of the current word state
        return " ".join(self.revealed)
    
    def matches_full_guess(self, guess):
        #compares the player's full word guess with the original word
        return guess.lower() == self.original
    

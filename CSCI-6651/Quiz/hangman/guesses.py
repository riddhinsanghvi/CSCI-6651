class Guess:# Base class for a player's guess
    def __init__(self, raw):
        self.raw = raw.strip().lower()

#Applies the guess to the Hangman game
    def apply(self, game):
        raise NotImplementedError("Subclass must implement apply()")
    
class LetterGuess(Guess):
    def apply(self, game):
        #Handles a single-letter guess
        letter = self.raw
        # Validate that input is a single alphabetic character
        if len(letter)!=1 or not letter.isalpha():
            print("\nINVALID letter guess.")
            return
         # Attempt to reveal the letter in the word
        correct = game.word.reveal_letter(letter)
        if not correct:
            game.figure.advance()


class WordGuess(Guess):
    #Handles a full word guess
    def apply(self, game):
        if game.word.matches_full_guess(self.raw):
            game.word.reveal_full()
        else:
            game.figure.advance()

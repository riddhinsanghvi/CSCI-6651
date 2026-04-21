from guesses import Guess, LetterGuess, WordGuess
from word import HangmanWord
from figure import HangmanFigure
from player import PlayerTurn


class HangmanGame:
    def __init__(self):
        # When the game is started these variables are created
        self.word = None
        self.figure = None
        self.turn = PlayerTurn() # handles each players turn

    def setup(self):
        #take input from the user
        text = input("Enter the secret word or Phrase: ").strip()
        self.word = HangmanWord(text)
        self.figure = HangmanFigure()

    def create_guess(self, raw):
        #Decide if the user entered a signle letter word or a multiple letter word
        if len(raw) == 1:
            return LetterGuess(raw)
        return WordGuess(raw)
    
    def play(self):
        self.setup()
        print("Game has started.")

        while True:
            #display the current correct guessed words
            print("Current Words:", self.word.display())
            #display the remaining parts of the body 
            print("Remaining Body Parts ",", ".join(self.figure.remaining_parts()))

            #Ask the player to guess the letters
            raw = self.turn.get_guess()

            if raw is None:
                #if the user chose to exit mid game
                print("Exiting Game!")
                return
            
            # Build the appropriate Guess object and apply it to the game state
            guess = self.create_guess(raw)
            guess.apply(self)

            # Check for win: all letters have been revealed
            if self.word.is_fully_revealed():
                print("You Guessed the word: ", self.word.display())
                print("WINNER!!!")
                break

            # Check for loss: all body parts have been drawn
            if self.figure.is_completed():
                print("\nThe Hangman is Completed. You LOSE :( ")
                print("The word was: ", self.word.original)
                break

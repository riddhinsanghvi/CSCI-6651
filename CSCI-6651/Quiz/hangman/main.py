from game import HangmanGame

def main():
    #The starting point of the game.
    while True:
        #Craeting a Hangman instance
        game = HangmanGame()
        # Start to play one game
        game.play()
        #Ask if the player wants to play again
        again = input("Do you want to play again (y/n) ?:").strip().lower()
        if again != "y":
            print("Bye-Bye!")
            break

if __name__ == "__main__":
    main()
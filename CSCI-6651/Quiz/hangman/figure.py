class HangmanFigure:
    def __init__(self):
        #List of body part to be revealed
        # The order is the sequence in which the hangman is drawn
        self.parts = ["head", "neck", "chest", "left arm","right arm","left leg","right leg","lower body"]
        # to tracks how many body parts have already been revealed
        self.index = 0

    def advance(self):
        #Move to the next body part if the hangman is not yet fully drawn.
        if not self.is_completed():
            self.index +=1
    
    def remaining_parts(self):
        #Returns a list of body parts that have not yet been revealed.
        return self.parts[self.index :]
    
    def is_completed(self):
        # Checks if all parts of the hangman have been revealed.
        return self.index >=len(self.parts)

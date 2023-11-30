import random
# TODO: REVIEW - make sure you have a line space between your import statements and class definition
class Hangman:

    def __init__(self, word_list, num_lives=5):
    
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = self.pick_random_word()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def pick_random_word(self):
        return random.choice(self.word_list)
    
    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess

            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")


    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")

            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

# TODO: REVIEW - in this game, it would be good for the player to be able to see the self.word_guessed variable each time they make a guess
# it would also be good for them to see the list of letters they've already guess as well as the number of lives they have left even if they make a correct guess or a repeated guess.

# TODO: REVIEW - you can put this code in an 'if __name__ == "__main__":' statement so that it will only run if this file is called directly, not when it is imported as a module to another file.
#Example usage:
# word_list = ['apple', 'banana', 'orange', 'grape']
# hangman_game = Hangman(word_list)
# hangman_game.ask_for_input()
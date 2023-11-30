import random

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
        check_list =[]
        
        for string in self.word_list:
            words = string.split()  
            for i, word in enumerate(words):
                if guess in word:
                    check_list.append(True)
                    self.word_guessed[i] = guess
                else:
                    check_list.append(False)
                    

        if any(check_list):
            print(f"Good guess! {guess} is in the word.")
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
                print(self.list_of_guesses)
                print(f"You have {self.num_lives} lives left.")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


#Example usage:
if __name__ == "__main__":
    word_list = ['apple', 'banana', 'orange', 'grape']
    hangman_game = Hangman(word_list)
    hangman_game.ask_for_input()
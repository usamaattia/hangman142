import random

fruits= ["pears", "banana", "grapes", "watermelons", "orange"]
word_list = fruits
print(word_list)

word = random.choice(word_list)
print(word)



def check_guess(guess):
    guess = guess.lower()
    check_list =[]
    for string in word_list:
        words = string.split()  # Split the string into a list of words
        for word in words:
            if guess in word:
                check_list.append(True)
            else:
                check_list.append(False)
                

    if any(check_list):
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


        

def ask_for_input():
    while True:    
        guess = input("Guess a letter: ")

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
        else:
            check_guess(guess)
            break

ask_for_input()


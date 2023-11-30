import random

# TODO: REVIEW - add a space after each comma
# TODO: REVIEW - it's best to make these all the same casing for consistency, so you should lowercase the "O" in "Orange"
fruits= ["pears","banana","grapes","watermelons","Orange"]
word_list = fruits
print(word_list)

word = random.choice(word_list)
print(word)



def check_guess(guess):
    guess = guess.lower()
    # TODO: REVIEW - this line isn't quite right. It's currently checking whether the letter you've guessed is one of the words in the word list (this will never be true)
    # You actually need to check whether the guess is in the selected word - what do you need to change to fix this?
    if guess in word_list:
        print(f"Good guess! {guess} is in the word.")

    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


        

def ask_for_input():
    # TODO: REVIEW - you might want to consider wrapping all the code here within the while True loop so that you don't have to repeat 'guess = input()'
    guess = input("guess the letter:")
    # TODO: REVIEW - you only need 'guess' in the brackets here, not 'guess=guess' because 'guess' is a positional argument, not a keyword argument
    # You should also think about what order you want things to run in. Ideally, you should first validate the guess and then if valid, check whether the guess is in the word
    check_guess(guess=guess)
    while True:
        # TODO: REVIEW - '& len(guess)!=0' is redundant here - can you see why?
        if len(guess)==1 & guess.isalpha() & len(guess)!=0:
            print("Good guess!")
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
            guess = input("guess the letter: ")

    
ask_for_input()


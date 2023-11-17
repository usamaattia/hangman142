import random


fruits= ["pears","banana","grapes","watermelons","Orange"]
word_list = fruits
print(word_list)

word = random.choice(word_list)
print(word)



def check_guess(guess):
    guess = guess.lower()
    if guess in word_list:
        print(f"Good guess! {guess} is in the word.")

    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


        

def ask_for_input():
    guess = input("guess the letter:")
    check_guess(guess=guess)
    while True:
        if len(guess)==1 & guess.isalpha() & len(guess)!=0:
            print("Good guess!")
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
            guess = input("guess the letter: ")

    
ask_for_input()


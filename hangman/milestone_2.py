import random

# TODO: REVIEW - add a space after each comma
# TODO: REVIEW - it's best to make these all the same casing for consistency, so you should lowercase the "O" in "Orange"
fruits= ["pears", "banana", "grapes", "watermelons", "orange"]
word_list = fruits
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("write a letter: ")

if len(guess)==1 & guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
import random


fruits= ["pears","banana","grapes","watermelons","Orange"]
word_list = fruits
print(word_list)

word = random.choice(word_list)
print(word)

guess = input("write a letter: ")

if len(guess)==1 & guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
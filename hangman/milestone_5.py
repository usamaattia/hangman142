from milestone_4 import Hangman

def play_game(word_list):
    # TODO: REVIEW - you can define 'num_lives = 6' within the brackets when your create your instance of the Hangman class on line 6
    # This is because num_lives is a keyword argument
    num_lives = 6
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            # TODO: REVIEW - it would be good to print out the word the player was guessing so that they know the answer even though they lost
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            # TODO: REVIEW - it would be good to print out the word the player was guessing to confirm to the player that they did guess the correct word
            break

word_list = ['apple', 'banana', 'orange', 'grape']
play_game(word_list)
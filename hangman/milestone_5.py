from milestone_4 import Hangman

def play_game(word_list):

    game = Hangman(word_list, num_lives=6)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            print(f"the word you are guessing is {game.word}")
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            print(f"the word you are guessing is {game.word}")
            break

word_list = ['apple', 'banana', 'orange', 'grape']
play_game(word_list)

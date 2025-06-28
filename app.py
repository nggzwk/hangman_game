#import modules
from words import words
import random

# select the word
def select_word():
    word = random.choice(words)
    return word.upper()

def play_hangman(word):
    word_completion = "_ " * len(word)  # create a string of underscores
    guessed = False
    guessed_letters = []
    guessed_words = []
    attempts = 6  # number defined on the scope

# welcoming message
    print("Welcome to Hangman!")
    print(show_status(attempts))
    print(f"This is the word: {word_completion}")

# while user has not guessed the word and attempts are left
    while not guessed and attempts > 0:
        guess = input("Please guess a word or a letter: ").upper()
        print(guess)

# check game status
def show_status(attempts):
    stages = [
        """
            -----
            |   |
            |   O
            |  \|/
            |  / \
            -
        """,
        """
            -----
            |   |
            |   O
            |  \|/
            |  /
            -
        """,
        """
            -----
            |   |
            |   O
            |  /|
            |
            -
        """,
        """
            -----
            |   |
            |   O
            |   |
            |
            -
        """,
        """
            -----
            |   |
            |   O
            |
            |
            -
        """,
        """
            -----
            |   |
            |
            |
            |
            -
        """,
        """
            -----
            
            
            
            
            
        """,
    ]

    return stages[attempts]

#start the game
def start_game():
    word = select_word()
    play_hangman(word)

start_game()
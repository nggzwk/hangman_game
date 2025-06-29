#import modules
from words import words
import random

# select the word
def select_word():
    word = random.choice(words)
    return word.upper()

def play_hangman(word):
    word_completion = "_" * len(word)  # create a string of underscores
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
    
    # one letter or full word
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"Letter already guessed. Try again. You have {attempts} attempts left.")
            elif guess not in word:
                print(f"Sorry, {guess} is not in the word. You have {attempts - 1} attempts left.")
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print(f"Nice! {guess} is in the word.")
                guessed_letters.append(guess)
                # update the word completion
                word_list = list(word_completion)
                index = [ i for i, letter in enumerate(word) if letter == guess ]
                for i in index:
                    word_list[i] = guess
                word_completion = "".join(word_list)
                print(' '.join(word_completion))

                if "_" not in word_completion:
                    guessed = True
                    print("Congratulations! You've guessed the word!")
                    
        # complete word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}. Try again. You have {attempts} attempts left.")
            elif guess != word:
                print(f"Sorry, {guess} is not the word. You have {attempts - 1} attempts left.")
                attempts -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
                print("Congratulations! You've guessed the word!")
        
        # invalid attempt
        else:
            print("Invalid attempt. Please enter a single letter or a full word.")

        print(show_status(attempts))
        print(' '.join(word_completion))

    # end the game
    if guessed:
        print("Congrats! You've guessed the word!")
    else:
        print(f"Sorry, you've run out of attempts. The word was {word}. Better luck next time!")

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

    while input("Do you want to play again? (Y/N): ").upper() == "Y":
        word = select_word()
        play_hangman(word)

start_game()
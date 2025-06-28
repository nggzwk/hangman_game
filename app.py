#import modules
from words import words
import random

# select the word
def select_word():
    word = random.choice(words)
    return word.upper()

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


#import modules
from words import words
import random

# select the word
def select_word():
    word = random.choice(words)
    return word.upper()

test = select_word()
print(f"Selected word: {test}")
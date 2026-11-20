import random

# Game for guessing a word from a list of words. The player then guess the letters one at a time. The player has 7 attempts to guess the correct word. After each guess, the program will provide feedback on whether the guess is correct or not.
# Correct letters will be revealed in the word, while incorrect letters will be counted as attempts. The game ends when the player either guesses the word correctly or runs out of attempts. Note that the player does not lose an attempt for guessing a letter that has already been guessed or correct.

# introduction
name = input("What is your name? ")
print(f"Hello {name}! Welcome to the Word Guessing Game!\n")

# list of words to choose from
words = ["python", "programming", "computer", "science", "algorithm", "function", "variable", "loop", "condition", "data"]
word = random.choice(words)

# function to display the rules of the game
def display_rules():
    print("I have selected a word from a list of words.")
    print("You have 7 attempts to guess the word by guessing one letter at a time.\n")
    print("After each guess, I will reveal the correct letters in the word and count incorrect letters as attempts.\n")
    print("Let's begin!\n")
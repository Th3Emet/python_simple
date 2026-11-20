import random

# This is a simple number guessing game where the player has to guess a randomly generated number between 1 and 100.
# The player has seven attempts to guess the correct number. After each guess, the program will provide feedback on whether the guess is too high, too low, or correct.

def display_rules():
        print("Welcome to the Number Guessing Game! \n")
        print("I have selected a number between 1 and 100.")
        print("You have 7 attempts to guess it.\n")

def play_game(number, attempts = 1):
    if attempts > 7:
        print("Sorry, you've used all your attempts. The correct number was:", number)
        return

    try:
        guess = int(input(f"Attempt {attempts}: Please enter your guess (1-100): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")
        return play_game(number, attempts)

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.\n")
        return play_game(number, attempt)

    check_guess = lambda guess, number: "correct" if guess == number else "too low" if guess < number else "too high"
    
    result = check_guess(guess, number)

    if result == "correct":
        print("Congratulations! You've guessed the correct number.")
        print(f"It took you {attempts} attempts to guess the number.")
        return
    elif result == "too low":
        print("Your guess is too low. Try with a larger number.\n")
    else:
        print("Your guess is too high. Try with a smaller number.\n")

    play_game(number, attempts + 1)

# start the game
start_game = input("Do you want to play the Number Guessing Game? (yes/no): ").strip().lower()
if start_game == "yes":
   display_rules()
   number = random.randint(1, 100)
   play_game(number)
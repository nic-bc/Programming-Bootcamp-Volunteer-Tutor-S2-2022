# to generate a random integer
from random import randint


# function to check what message to display
def play(start = True) -> str:
    """
    Takes in nothing and outputs a string.

    Parameters
    ----------
    start: bool -> default value of argument is set to "True" to automatically start the game when the code is executed

    How it works?
    - with a random number generated and an input (guess) given by the user, it will output "lower" if the user's
      guess is higher than the random number generated, output "higher" if the user's guess is lower than the
      random number generated, and output "correct" if the user's guess is equivalent to the random number generated
    - if the input(guess) is more than 100 or is a string, symbol, or float (anything else other than an integer),
      it will notify the user that it's an invalid input

    For example, if the number generated is 50:
    1: when we guess 60, output will be "lower"
    2: when we guess 30, output will be "higher"
    3: when we guess "I honestly don't get this task", output will be "invalid input"
    4: when we guess 50, output will be "correct"
    """

    # create random number (from 1 to 100) to be guessed and store that number in variable "num_to_guess"
    num_to_guess = randint(1,100)
    message("Guess the number :)")          # prompt to start game

    while start:        # i.e. while True
        # prompt user to input an number using input() and store that input in variable "guess"
        guess = input("Insert a number between 1 to 100: ")

        # first, we validate the guess
        # if input is invalid (e.g. a symbol or sting, etc or if number is more than 100)
        # we prompt the user to re-input an integer
        if (guess.isnumeric() == False) or (int(guess) > 100):
            message("Invalid Input! Please input an integer smaller than or equal to 100")

        # if guess is more than the number to guess, we notify the user that the guess should be lower
        elif int(guess) > num_to_guess:
            message("False. Number is lower than that :(")

        # if guess is lesser than the number to guess, we notify the user that the guess should be higher
        elif int(guess) < num_to_guess:
            message("False. Number is higher than that :(")

        # if the guess is right, we notify the user that it's right and break to terminate loop
        elif int(guess) == num_to_guess:
            message("Correct!! " + guess + " is the answer!")
            break


# function to print a message
def message(message_to_display: str) -> str:
    """
    - Takes in a string and outputs a string.
    - helps us to print the message we want to display

    Parameters
    ----------
    message_to_display: str -> the message we want to display
    """

    # prints the message in a new line due to "\n"
    print("\n" + message_to_display)


# to start playing the game
play()
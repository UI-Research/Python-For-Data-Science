# the following is how you import a module you want to use that isn't automatically included
# We're going to use the "randint" function from the "random" module
# So that we can simulate the computer playing Rock Paper Scissors

import random

def main():
    user_choice = input("Would you like to play Rock (R), Paper (P), or Scissors(S)? ")
    computer_choice = random.randint(1, 3)
    # Now you'll need to assign the random integer to represent one of Rock, Paper, and Scissors
    # And determine the winner between the user and the computer





# Call the function we created above
main()

import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)
guess_count = 0

print("Welcome to the Guess the Number Game!")
print("I have picked a number between 1 and 100. Try to guess it!")
print("Type 'exit' to quit the game at any time.")

# Game loop
while True:
    # Ask the user to guess a number or type 'exit' to quit
    user_input = input("Enter your guess: ")

    # Check if the user wants to quit
    if user_input.lower() == 'exit':
        print(f"Game over. The number was {number_to_guess}.")
        print(f"You took {guess_count} guesses.")
     


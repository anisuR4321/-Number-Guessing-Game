import random

def play_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Initialize variables
    guess = 0
    attempts = 0

    # Game loop
    while guess != secret_number:
        # Get user input
        guess_input = input("Enter your guess: ")
        
        # Convert input to integer
        try:
            guess = int(guess_input)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # Increment attempts counter
        attempts += 1
        
        # Check guess
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")

    print("Thanks for playing!")

# Automatically run the game when the script is executed
if __name__ == "__main__":
    play_guessing_game()

# So I dont have to put random every time I want to use it
from random import randrange

def play_game():
    # Game introduction
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the random number between 0 and 100.")
    print("You have 10 total guesses. Good luck!\n")

    # Generate a random number between 0 and 100
    random_number = randrange(0, 101)

    # Counter to track attempts
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        # Show the attempt number in the input message
        guess = input(f"Guess #{attempts + 1}: Enter a number between 0 and 100: ")

        # Ensure valid integer input
        if not guess.isdigit():
            print("Invalid input. Please enter an integer number.\n")
            continue

        guess = int(guess)
        attempts += 1

        if guess == random_number:
            print(f"Awsome Sauce! You guessed the number {random_number} in {attempts} tries.\n")
            break
        else:
            if attempts < max_attempts:
                if guess < random_number:
                    print("Incorrect. Your guess is too LOW. Try again.\n")
                else:
                    print("Incorrect. Your guess is too HIGH. Try again.\n")
            else:
                print(f" Please try again you didnt guess the right number! You ran out of tries. The number was {random_number}.\n")

# Main loop to allow replay
while True:
    play_game()
    again = input("Would you like to play again? (y/n): ").strip().lower()
    while again not in ['y', 'n']:
        again = input("Invalid input. Please enter 'y' for yes or 'n' for no: ").strip().lower()
    if again == 'n':
        print("Thanks for playing! Goodbye.\n")
        break

# Required completion statement
print("Completed by, Aldo Dillard Jefferson")
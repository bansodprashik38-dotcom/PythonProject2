import random


def play_game():
    secret_number = random.randint(1, 20)
    attempts = 5

    print("Number Guessing Game")
    print("I am thinking of a number between 1 and 20.")
    print(f"You have {attempts} chances to guess it.")

    for chance in range(1, attempts + 1):
        while True:
            guess_text = input(f"\nChance {chance}: Enter your guess: ")

            if guess_text.isdigit():
                guess = int(guess_text)
                break

            print("Please enter a valid number.")

        if guess == secret_number:
            print("You won! You guessed the correct number.")
            return

        if guess < secret_number:
            print("Too low.")
        else:
            print("Too high.")

    print(f"\nGame over! The number was {secret_number}.")


play_game()

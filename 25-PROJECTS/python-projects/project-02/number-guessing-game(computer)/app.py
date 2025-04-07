import random

def number_guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 0
    max_attempts = 5
    
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                return
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
                
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"You have {remaining} attempts remaining.")
            else:
                print("No more attempts left.")
                
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"\nGame over! The secret number was {secret_number}.")

number_guessing_game()
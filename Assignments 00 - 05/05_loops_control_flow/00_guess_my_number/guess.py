import random
print("Welcome to Guess My Number!")
com_guess = random.randint(1, 99)

print("I am thinking of a number between 1 and 99.")

user_guess= int(input("Enter your guess: "))

while user_guess != com_guess:
   
    if user_guess < com_guess:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

    user_guess = int(input("Enter your guess: "))
print("Congratulations! You guessed my number.")
print("The number was", com_guess)
# This is a simple number guessing game where the computer randomly selects a number between 1 and 99, and the user has to guess it.
import random

class HumanVsComputerGuessGame:
    def __init__(self, low=1, high=100):
        self.low = low
        self.high = high
        self.attempts = 0

    def human_guesses(self):
        number = random.randint(self.low, self.high)
        print(f"\nI (computer) have chosen a number between {self.low} and {self.high}. Can you guess it?")
        while True:
            try:
                guess = int(input("Your guess: "))
            except ValueError:
                print("Please enter a valid integer.")
                continue
            self.attempts += 1
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print(f"Congrats! You guessed it in {self.attempts} attempts.")
                break

    def computer_guesses(self):
        print(f"\nThink of a number between {self.low} and {self.high}, and I'll try to guess it!")
        input("Once you have your number, press Enter... ")
        low, high = self.low, self.high
        while True:
            guess = (low + high) // 2
            self.attempts += 1
            response = input(f"Is your number {guess}? (enter 'h' if too high, 'l' if too low, 'c' if correct): ").lower()
            if response == 'h':
                high = guess - 1
            elif response == 'l':
                low = guess + 1
            elif response == 'c':
                print(f"Yay! I guessed your number in {self.attempts} attempts.")
                break
            else:
                print("Please respond with 'h', 'l', or 'c'.")

    def play(self):
        self.attempts = 0
        self.human_guesses()
        self.attempts = 0
        self.computer_guesses()

if __name__ == '__main__':
    game = HumanVsComputerGuessGame(1, 100)
    game.play()

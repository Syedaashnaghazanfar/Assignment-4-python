import random

class TwoPlayerGuessGame:
    def __init__(self, low=1, high=100):
        self.low = low
        self.high = high
        self.target = random.randint(self.low, self.high)
        self.attempts = {"Player 1": 0, "Player 2": 0}
        self.current = "Player 1"

    def switch_player(self):
        self.current = "Player 2" if self.current == "Player 1" else "Player 1"

    def play(self):
        print(f"\nI'm thinking of a number between {self.low} and {self.high}."
              " Players will take turns guessing.")
        while True:
            try:
                guess = int(input(f"{self.current}, enter your guess: "))
            except ValueError:
                print("Invalid input; please enter an integer.")
                continue

            self.attempts[self.current] += 1

            if guess < self.target:
                print("Too low!")
            elif guess > self.target:
                print("Too high!")
            else:
                print(f"\nCongrats {self.current}! You guessed the number in {self.attempts[self.current]} attempts.")
                break

            # Switch turns
            self.switch_player()

if __name__ == "__main__":
    print("Welcome to Two-Player Guess the Number Game!")
    game = TwoPlayerGuessGame(1, 100)
    game.play()

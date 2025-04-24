import random
import string

class Hangman:
    def __init__(self, word_list=None, max_attempts=6):
        if word_list is None:
            self.word_list = [
                'python', 'developer', 'openai', 'hangman', 'challenge',
                'artificial', 'intelligence', 'function', 'variable', 'syntax'
            ]
        else:
            self.word_list = word_list
        self.max_attempts = max_attempts
        self.secret_word = random.choice(self.word_list)
        self.guessed_letters = set()
        self.wrong_attempts = 0

    def display_progress(self):
        display = ' '.join(
            [letter if letter in self.guessed_letters else '_' for letter in self.secret_word]
        )
        print(f"Word: {display}")
        print(f"Wrong attempts: {self.wrong_attempts}/{self.max_attempts}\n")

    def guess(self, letter):
        if letter in self.guessed_letters:
            print("You've already guessed that letter. Try another.")
        elif letter in self.secret_word:
            print(f"Good guess! '{letter}' is in the word.")
            self.guessed_letters.add(letter)
        else:
            print(f"Sorry, '{letter}' is not in the word.")
            self.guessed_letters.add(letter)
            self.wrong_attempts += 1

    def is_won(self):
        return all(letter in self.guessed_letters for letter in self.secret_word)

    def is_lost(self):
        return self.wrong_attempts >= self.max_attempts

    def play(self):
        print("\nWelcome to Hangman! Try to guess the word letter by letter.")
        while not self.is_won() and not self.is_lost():
            self.display_progress()
            guess = input("Enter a letter: ").lower()
            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print("Please enter a single alphabetical character.")
                continue
            self.guess(guess)

        if self.is_won():
            print(f"\nCongratulations! You guessed the word '{self.secret_word}'.")
        else:
            print(f"\nGame over. The word was '{self.secret_word}'. Better luck next time!")

if __name__ == '__main__':
    game = Hangman()
    game.play()

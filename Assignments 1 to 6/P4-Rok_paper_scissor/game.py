import random

class RockPaperScissors:
    def __init__(self, rounds=3):
        self.rounds = rounds
        self.choices = ['rock', 'paper', 'scissors']
        self.score = {'Player 1': 0, 'Player 2': 0}

    def get_winner(self, choice1, choice2):
     
        if choice1 == choice2:
            return 'Tie'
        wins = {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock'
        }
        if wins[choice1] == choice2:
            return 'Player 1'
        else:
            return 'Player 2'

    def play_round(self, round_num):
        print(f"\nRound {round_num}:")
        while True:
            p1 = input("Player 1, enter rock, paper, or scissors: ").lower()
            if p1 in self.choices:
                break
            print("Invalid choice.")
        while True:
            p2 = input("Player 2, enter rock, paper, or scissors: ").lower()
            if p2 in self.choices:
                break
            print("Invalid choice.")

        winner = self.get_winner(p1, p2)
        if winner == 'Tie':
            print(f"Both chose {p1}. It's a tie!")
        else:
            print(f"{winner} wins! {p1} vs {p2}.")
            self.score[winner] += 1

    def play(self):
        print(f"Welcome to Rock, Paper, Scissors! Best of {self.rounds} rounds.")
        for i in range(1, self.rounds + 1):
            self.play_round(i)
        print("\nFinal Score:")
        print(f"Player 1: {self.score['Player 1']} | Player 2: {self.score['Player 2']}")
        if self.score['Player 1'] > self.score['Player 2']:
            print("Player 1 is the overall winner!")
        elif self.score['Player 2'] > self.score['Player 1']:
            print("Player 2 is the overall winner!")
        else:
            print("It's an overall tie!")

if __name__ == '__main__':
    try:
        rounds = int(input("Enter the number of rounds to play: "))
    except ValueError:
        rounds = 3
    game = RockPaperScissors(rounds)
    game.play()

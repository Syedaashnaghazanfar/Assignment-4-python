def print_board(board):
    # Print the Tic-Tac-Toe board
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def main():
    # Initial game setup
    board = [" " for _ in range(9)]  # Empty Tic-Tac-Toe board
    current_player = "X"  # Starting player is X
    game_over = False

    while not game_over:
        print_board(board)
        move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1

        if board[move] != " ":
            print("That position is already taken! Try again.")
            continue

        # Make the move
        board[move] = current_player

        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        elif " " not in board:
            # Check for draw (no more spaces available)
            print_board(board)
            print("It's a draw!")
            game_over = True
        else:
            # Switch players
            current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
5
#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
        col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

        if 0 <= row < 3 and 0 <= col < 3:  # Check if row and column are valid
            if board[row][col] == " ":
                board[row][col] = player
                # Toggle player after successful move
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        else:
            print("Invalid row or column! Try again.")

    print_board(board)
    # Print the opposite player as the winner
    winner = "O" if player == "X" else "X"
    print("Player " + winner + " wins!")

tic_tac_toe()
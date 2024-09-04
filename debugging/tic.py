#!/usr/bin/python3

def print_board(board):
    """
    Prints the current state of the board.

    Parameters:
    board (list of list of str): The tic-tac-toe board.

    Returns:
    None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner in the current board configuration.

    Parameters:
    board (list of list of str): The tic-tac-toe board.

    Returns:
    bool: True if there is a winner, False otherwise.
    """
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def check_tie(board):
    """
    Checks if the game is a tie (no more empty spaces and no winner).

    Parameters:
    board (list of list of str): The tic-tac-toe board.

    Returns:
    bool: True if the game is a tie, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    The main function to play the tic-tac-toe game. Handles player input, updates the board, 
    and checks for winning or tie conditions.

    Returns:
    None
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Error: Please enter a valid row and column between 0 and 2.")
                continue

            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
            
            board[row][col] = player
            
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break

            if check_tie(board):
                print_board(board)
                print("The game is a tie!")
                break

            # Switch player
            player = "O" if player == "X" else "X"

        except ValueError:
            print("Error: Please enter numbers only.")
        except IndexError:
            print("Error: Please enter a valid row and column between 0 and 2.")

if __name__ == "__main__":
    tic_tac_toe()
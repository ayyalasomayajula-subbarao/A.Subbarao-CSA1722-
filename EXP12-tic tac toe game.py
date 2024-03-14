def print_board(board):
    """Prints the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Check if the current player has won."""
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def get_move():
    """Gets valid user move."""
    while True:
        try:
            row = int(input("Enter row number (0-2): "))
            col = int(input("Enter column number (0-2): "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Invalid input! Row and column must be between 0 and 2.")
        except ValueError:
            print("Invalid input! Please enter integers.")

def tic_tac_toe():
    """Main function to play Tic Tac Toe."""
    board = [[" "]*3 for _ in range(3)]
    players = ['X', 'O']
    current_player = 0
    moves = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        row, col = get_move()

        if board[row][col] == " ":
            board[row][col] = players[current_player]
            moves += 1
            print_board(board)
            if check_winner(board, players[current_player]):
                print(f"Player {players[current_player]} wins!")
                break
            elif moves == 9:
                print("It's a draw!")
                break
            current_player = 1 - current_player
        else:
            print("That cell is already occupied!")

if __name__ == "__main__":
    tic_tac_toe()

def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))
    print()
def move(board, direction):
    empty_i, empty_j = find_empty(board)
    if direction == 'up' and empty_i > 0:
        board[empty_i][empty_j], board[empty_i - 1][empty_j] = board[empty_i - 1][empty_j], board[empty_i][empty_j]

    return board
def find_empty(board):
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == 0:
                return i, j
initial_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 0, 8]
]
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
print("Initial State:")
print_board(initial_state)
print("Move 'up':")
print_board(move(initial_state,'up'))

print("Goal State:")
print_board(goal_state)

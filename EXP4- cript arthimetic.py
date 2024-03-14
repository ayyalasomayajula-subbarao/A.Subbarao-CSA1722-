import itertools

def is_valid(puzzle, solution):
    equation = puzzle
    for key, value in solution.items():
        equation = equation.replace(key, str(value))
    try:
        return eval(equation)
    except ZeroDivisionError:
        return False

def solve_cryptarithmetic(puzzle):
    unique_chars = set(char for char in puzzle if char.isalpha())
    words = [word for word in puzzle.split() if word.isalpha()]
    
    for perm in itertools.permutations("0123456789", len(unique_chars)):
        solution = dict(zip(unique_chars, perm))
        
        if all(solution[word[0]] != '0' for word in words) and is_valid(puzzle, solution):
            return {key: int(value) for key, value in solution.items()}
    
    return None

puzzle = "SEND + MORE == MONEY"

solution = solve_cryptarithmetic(puzzle)
if solution:
    print("Solution found:")
    for key, value in solution.items():
        print(f"{key} = {value}")
else:
    print("No solution found.")

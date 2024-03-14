from collections import deque

MAX_MISSIONARIES = 3
MAX_CANNIBALS = 3

def is_valid_state(state):
    m, c, b = state
    if m < 0 or c < 0 or m > MAX_MISSIONARIES or c > MAX_CANNIBALS:
        return False
    if m < c and m > 0:
        return False
    if MAX_MISSIONARIES - m < MAX_CANNIBALS - c and MAX_MISSIONARIES - m > 0:
        return False
    return True

def get_next_states(state):
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    next_states = []
    
    for dm, dc in moves:
        if state[2] == 1:
            new_state = (state[0] - dm, state[1] - dc, 0)
        else:
            new_state = (state[0] + dm, state[1] + dc, 1)
        
        if is_valid_state(new_state):
            next_states.append(new_state)
    
    return next_states

def bfs_missionaries_and_cannibals():
    start_state = (MAX_MISSIONARIES, MAX_CANNIBALS, 1)
    goal_state = (0, 0, 0)
    
    visited = set()
    queue = deque([(start_state, [])])  # State, Steps
    
    while queue:
        current_state, steps = queue.popleft()
        
        if current_state == goal_state:
            return steps + [(0, 0, 0)]
        
        visited.add(current_state)
        
        next_states = get_next_states(current_state)
        for next_state in next_states:
            if next_state not in visited:
                queue.append((next_state, steps + [current_state]))
                visited.add(next_state)
    
    return None

result = bfs_missionaries_and_cannibals()
if result:
    print("Steps to move all missionaries and cannibals:")
    for step in result:
        print(f"{step}")
else:
    print("No solution found.")

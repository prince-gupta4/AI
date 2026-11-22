from collections import deque

def solve_water_jug(jug1_cap, jug2_cap, target):
    # Queue stores the current state (jug1, jug2) and the path taken to reach it
    queue = deque([((0, 0), [(0, 0)])])
    # Set to keep track of visited states to avoid infinite loops
    visited = set([(0, 0)])
    
    while queue:
        (j1, j2), path = queue.popleft()
        
        # Check if the goal state is reached (2L water in the 4L jug)
        if j1 == target:
            print(f"Goal reached! Total steps: {len(path) - 1}\n")
            print("Steps taken:")
            for state in path:
                print(state)
            return True
            
        # Define all 6 possible production rules/moves
        moves = [
            (jug1_cap, j2),                 # 1. Fill Jug 1
            (j1, jug2_cap),                 # 2. Fill Jug 2
            (0, j2),                        # 3. Empty Jug 1
            (j1, 0),                        # 4. Empty Jug 2
            # 5. Pour from Jug 2 to Jug 1 until Jug 1 is full or Jug 2 is empty
            (min(j1 + j2, jug1_cap), j2 - (min(j1 + j2, jug1_cap) - j1)),
            # 6. Pour from Jug 1 to Jug 2 until Jug 2 is full or Jug 1 is empty
            (j1 - (min(j1 + j2, jug2_cap) - j2), min(j1 + j2, jug2_cap))
        ]
        
        for next_state in moves:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
                
    print("No solution possible.")
    return False

# Run the puzzle with a 4L jug, 3L jug, and target of 2L
solve_water_jug(jug1_cap=4, jug2_cap=3, target=2)

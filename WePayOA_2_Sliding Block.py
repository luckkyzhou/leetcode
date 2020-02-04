def movesToSolve (puzzle):
    # Write your code here
    row = len(puzzle)
    col = len(puzzle[0])

    # Convert input 2D array into a 1D array.
    start = []
    for i in range(row):
        for j in range(col):
            start.append(puzzle[i][j])
    start = tuple(start)

    # Use queue for BFS. And we store the (start array, the index of 0, depth = 0) to initialize it.
    queue = [(start, start.index(0), 0)]

    # Define a visited set to avoid repetition in BFS.
    visited = {start}

    # Define the solved puzzle status.
    target = tuple(list(range(0, row * col)))

    # BFS
    while queue:
        puzzle, position, depth = queue.pop(0)
        if puzzle == target: return depth

        # Due to the 1D array, the neighbor of 0 should be +- 1 or +- col.
        for direction in (1, -1, col, -col):
            neighbor = position + direction
            # Prevent the rightmost from the previous line and the leftmost from the next line change their positions.
            if abs(neighbor // col - position // col) + abs(neighbor % col - position % col) != 1: continue
            # Check whether new position is in range.
            if 0 <= neighbor < row * col:
                new_puzzle = list(puzzle)
                new_puzzle[position], new_puzzle[neighbor] = new_puzzle[neighbor], new_puzzle[position]
                new_puzzle = tuple(new_puzzle)
                if new_puzzle not in visited:
                    visited.add(new_puzzle)
                    queue.append((new_puzzle, neighbor, depth + 1))
    return -1

if __name__ == '__main__':
    res = movesToSolve([[1,4,2], [3,0,5], [6,7,8]])
    print(res)
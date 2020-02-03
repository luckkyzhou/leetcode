from typing import List
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        row = len(board)
        col = len(board[0])
        start = []
        for i in range(row):
            for j in range(col):
                start.append(board[i][j])
        start = tuple(start)
        queue = [(start, start.index(0), 0)]
        visited = {start}
        target = tuple(list(range(1, row * col)) + [0])

        while queue:
            board, position, depth = queue.pop(0)
            if board == target: return depth
            for direction in (1, -1, col, -col):
                neighbor = position + direction
                if abs(neighbor // col - position // col) + abs(neighbor % col - position % col) != 1: continue
                if 0 <= neighbor < row * col:
                    new_board = list(board)
                    new_board[position], new_board[neighbor] = new_board[neighbor], new_board[position]
                    new_board = tuple(new_board)
                    if new_board not in visited:
                        visited.add(new_board)
                        queue.append((new_board, neighbor, depth + 1))
        return -1

if __name__ == '__main__':
    solution = Solution()
    res = solution.slidingPuzzle([[3,2,4],[1,5,0]])
    print(res)
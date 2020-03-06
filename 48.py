from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                row, col = i, j
                rotMatrix = [0] * 4
                for k in range(4):
                    rotMatrix[k] = matrix[row][col]
                    row, col = col, n - row - 1
                for k in range(4):
                    matrix[row][col] = rotMatrix[(k - 1) % 4]
                    row, col = col, n - row - 1
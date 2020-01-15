from typing import List
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        if len(matrix) == 0: return
        self.rowCount = len(matrix)
        self.colCount = len(matrix[0])
        self.sumMatrix = [[0 for _ in range(self.colCount)] for _ in range(self.rowCount)]

        for i in range(self.rowCount):
            self.sumMatrix[i][0] = matrix[i][0]
            for j in range(1, self.colCount):
                self.sumMatrix[i][j] = self.sumMatrix[i][j - 1] + matrix[i][j]

    def update(self, row: int, col: int, val: int) -> None:
        self.matrix[row][col] = val
        curCol = col
        if col == 0:
            self.sumMatrix[row][col] = self.matrix[row][col]
            curCol += 1
        for j in range(curCol, self.colCount):
            self.sumMatrix[row][j] = self.sumMatrix[row][j - 1] + self.matrix[row][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1, row2 + 1):
            if col1 == 0: sum += self.sumMatrix[i][col2]
            else: sum += self.sumMatrix[i][col2] - self.sumMatrix[i][col1 - 1]
        return sum

if __name__ == '__main__':
    solution = NumMatrix([[1]])
    res = solution.sumRegion(0,0,0,0)
    print(res)
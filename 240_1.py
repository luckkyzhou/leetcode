class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix: return False

        height = len(matrix)
        width = len(matrix[0])
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            elif matrix[row][col] == target:
                return True
        return False
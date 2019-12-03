class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix: return False

        for i in range(min(len(matrix), len(matrix[0]))):
            vertical = self.binarySearch(matrix, target, i, True)
            horizontal = self.binarySearch(matrix, target, i, False)
            if vertical or horizontal: return True
        return False

    def binarySearch(self, matrix, target, start, vertical):
        low = start
        high = len(matrix) if vertical else len(matrix[0])

        while low < high:
            mid = low + (high - low) // 2
            if not vertical:
                if matrix[start][mid] < target:
                    low = mid + 1
                elif matrix[start][mid] > target:
                    high = mid
                elif matrix[start][mid] == target:
                    return True
            else:
                if matrix[mid][start] < target:
                    low = mid + 1
                elif matrix[mid][start] > target:
                    high = mid
                elif matrix[mid][start] == target:
                    return True
        return False
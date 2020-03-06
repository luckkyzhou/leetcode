from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            midVal = matrix[mid // n][mid % n]
            if midVal < target:
                left = mid + 1
            elif midVal > target:
                right = mid - 1
            elif midVal == target:
                return True
        return False
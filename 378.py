class Solution(object):

    def kthSmallest(self, matrix, k):

        # 求count是，从右上角往左下角遍历，O(N)
        def count(target, l):
            i = 0
            j = l - 1
            counter = 0
            while j >= 0 and i < l:
                if matrix[i][j] <= target:  # !!! 小于等于，必须包含相等，即便等于目标值的数量
                    counter += j + 1
                    i += 1
                else:
                    j -= 1
            return counter

        low = matrix[0][0]
        n = len(matrix)
        high = matrix[n - 1][n - 1]
        while low < high:
            mid = low + (high - low) >> 1
            c = count(mid, n)  # O(N)
            if c < k:  # 包含相等的数量小于k，才将中间值加1
                low = mid+1
            else:
                high = mid
        return high

if __name__ == '__main__':
    solution = Solution()
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    res = solution.kthSmallest(matrix,8)
    print(res)
from typing import List

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        n = len(A)
        left1, left2 = 0, 0
        count1, count2 = 0, 0
        visited_1, visited_2 = [0] * (len(A) + 1), [0] * (len(A) + 1)
        res = 0

        for right in range(n):
            if visited_1[A[right]] == 0:
                count1 += 1
            visited_1[A[right]] += 1
            if visited_2[A[right]] == 0:
                count2 += 1
            visited_2[A[right]] += 1
            while count1 > K:
                if visited_1[A[left1]] == 1:
                    count1 -= 1
                visited_1[A[left1]] -= 1
                left1 += 1
            while count2 > K - 1:
                if visited_2[A[left2]] == 1:
                    count2 -= 1
                visited_2[A[left2]] -= 1
                left2 += 1

            res += left2 - left1
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.subarraysWithKDistinct([1,2,1,2,3], 2)
    print(res)
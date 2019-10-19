from typing import List

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        difference = arr[-1] - arr[0]
        diff = difference // len(arr)
        start = arr[0]
        if start == 0 and diff == 0:
            return 0
        for i in range(len(arr)):
            start += diff
            if start not in arr:
                return start
from typing import List
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        low = lower - 1
        nums.append(upper + 1)  # 用来保证最后的num到upper的区间
        for num in nums:
            diff = num - low
            if diff == 2: res.append(str(num - 1))
            elif diff >= 2: res.append(str(low + 1) + "->" + str(num - 1))
            low = num
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.findMissingRanges([],1,1)
    print(res)
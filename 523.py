from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        sum = 0
        hashmap[0] = -1
        for i in range(len(nums)):
            sum += nums[i]
            if k != 0:
                sum = sum % k
            if sum in hashmap.keys():
                # 避免相邻的前缀和mod相同，即加了k本身
                if i - hashmap[sum] > 1:
                    return True
            else: hashmap[sum] = i
        return False

if __name__ == '__main__':
    solution = Solution()
    res = solution.checkSubarraySum([4,6],6)
    print(res)
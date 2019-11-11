from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        queue = []
        res = []
        for i in range(k):
            queue.append(nums[i])
        queue.sort()
        if len(queue) & 1 == 1:
            res.append(queue[len(queue) // 2])
        else:
            res.append((queue[len(queue) // 2 - 1] + queue[len(queue) // 2]) / 2)

        for i in range(k, len(nums)):
            locate = self.binarySearch(queue, 0, len(queue) - 1, nums[i])
            queue.insert(locate, nums[i])
            queue.pop(queue.index(nums[i - k]))
            if len(queue) & 1 == 1:
                res.append(queue[len(queue) // 2])
            else:
                res.append((queue[len(queue) // 2 - 1] + queue[len(queue) // 2]) / 2)
        return res

    def binarySearch(self, nums, left, right, target):
        if target <= nums[left]:
            return left
        if target >= nums[right]:
            return right + 1
        if right - left == 1:
            return right
        median = (right - left) // 2 + left
        if target <= nums[median]:
            right = median
        else:
            left = median
        return self.binarySearch(nums, left, right, target)

if __name__ == '__main__':
    solution = Solution()
    res = solution.medianSlidingWindow([7,0,3,9,9,9,1,7,2,3],6)
    #res = solution.medianSlidingWindow([1,3,-1,-3,5,3,6,7],3)
    print(res)
# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1:List[int], nums2:List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        nums1.extend(nums2)
        nums1.sort()

        # 奇数二进制最后一位是1，偶数二进制最后一位是0
        # 二进制右移一位=除以2的1次方
        if (m + n) & 1:
            return nums1[(m + n - 1) >> 1]
        else:
            return (nums1[(m + n -1) >> 1] + nums1[(m + n) >> 1]) / 2

if __name__ == '__main__':
    find = Solution()
    output = find.findMedianSortedArrays([1,2], [3,4])
    print(output)
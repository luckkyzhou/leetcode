from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        len1 = m - 1
        len2 = n - 1
        lenA = m + n - 1

        while len1 >= 0 and len2 >= 0:
            if nums1[len1] >= nums2[len2]:
                nums1[lenA] = nums1[len1]
                len1 -= 1
            else:
                nums1[lenA] = nums2[len2]
                len2 -= 1
            lenA -= 1
        nums1[:len2 + 1] = nums2[:len2 + 1]

if __name__ == '__main__':
    solution = Solution()
    solution.merge([1,2,3,0,0,0],3,[2,5,6],3)
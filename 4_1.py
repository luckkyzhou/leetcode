class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        def getKthElement(k):
            idx1, idx2 = 0, 0
            while True:
                if idx1 == m:
                    return nums2[idx2 + k - 1]
                if idx2 == n:
                    return nums1[idx1 + k - 1]
                if k == 1:
                    return min(nums1[idx1], nums2[idx2])

                newIdx1 = min(idx1 + k // 2 - 1, m - 1)
                newIdx2 = min(idx2 + k // 2 - 1, n - 1)
                num1, num2 = nums1[newIdx1], nums2[newIdx2]
                if num1 <= num2:
                    k -= newIdx1 - idx1 + 1
                    idx1 = newIdx1 + 1
                else:
                    k -= newIdx2 - idx2 + 1
                    idx2 = newIdx2 + 1
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            a = float(getKthElement(totalLength // 2))
            b = float(getKthElement(totalLength // 2 + 1))
            return (a + b) / 2
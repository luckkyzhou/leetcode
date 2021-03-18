class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)

        def getKthElement(k):
            idx1 = 0
            idx2 = 0

            while k >= 1:
                if idx1 == m:
                    return nums2[idx2 + k - 1]
                if idx2 == n:
                    return nums1[idx1 + k - 1]
                if k == 1:
                    return min(nums1[idx1], nums2[idx2])

                new_idx1 = min(idx1 + k//2 - 1, m - 1)
                new_idx2 = min(idx2 + k//2 - 1, n - 1)

                if nums1[new_idx1] <= nums2[new_idx2]:
                    k -= (new_idx1 - idx1 + 1)
                    idx1 = new_idx1 + 1
                else:
                    k -= (new_idx2 - idx2 + 1)
                    idx2 = new_idx2 + 1

        if (m+n) & 1 == 1:
            return getKthElement((m+n)//2 + 1)
        else:
            return float((getKthElement((m+n)//2) + getKthElement((m+n)//2 + 1))) / 2

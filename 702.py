class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) == target: return 0
        left, right = 0, 1

        while reader.get(right) < target:
            left = right
            right <<= 1

        while left < right:
            mid = left + (right - left) // 2
            if reader.get(mid) == target:
                return mid
            elif reader.get(mid) > target:
                right = mid
            elif reader.get(mid) < target:
                left = mid + 1
        return left if reader.get(left) == target else -1
class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def countNode(idx):
            count = 0
            cur = idx
            next = idx + 1
            while cur <= n:
                count += min(n+1, next) - cur
                cur *= 10
                next *= 10
            return count

        i = 1
        p = 1
        while p < k:
            count = countNode(i)
            if count + p > k:
                i *= 10
                p += 1
            else:
                i += 1
                p += count
        return p

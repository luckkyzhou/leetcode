class Solution:
    def kDifference(self, a, k):
        b = set(a)
        a = list(b)
        a.sort()
        count = 0

        for num in a:
            if num + k in a:
                count += 1
        return count
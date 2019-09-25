class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            y = -x
            mid = str(y)
            mid = mid[::-1]
            res = -int(mid)
        else:
            mid = str(x)
            mid = mid[::-1]
            res = int(mid)

        if abs(res) > 2147483647:
            return 0
        else:
            return res
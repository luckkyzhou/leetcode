class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0: return True
        elif x < 0 or x % 10 == 0: return False

        revertX = 0
        while x > revertX:
            revertX *= 10
            revertX += (x % 10)
            x //= 10
        return x == revertX or x == revertX // 10
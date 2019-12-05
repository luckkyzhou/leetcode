import math
class Solution:
    def primePalindrome(self, N: int) -> int:
        def isPrime(N: int) -> bool:
            if N == 2 or N == 3: return True
            if N % 6 != 1 and N % 6 != 5: return False

            for i in range(5, int(math.sqrt(N)) + 1, 6):
                if N % i == 0 or N % (i + 2) == 0: return False
            return True

        def isReverse(N: int) -> bool:
            temp = str(N)
            if temp == temp[::-1]: return True
            else: return False

        i = N if N > 1 else N + 1
        while i < 2 * (10 ** 8):
            if len(str(i)) == 4:
                i = 10 ** 4
                continue
            if len(str(i)) == 6:
                i = 10 ** 6
                continue
            if len(str(i)) == 8:
                i = 10 ** 8
                continue
            if isReverse(i):
                if isPrime(i):
                    return i
            if i > 10:
                if i % 6 == 0: i += 1
                elif i % 6 == 1: i += 4
                elif i % 6 == 5: i += 2
                else: i += (5 - i % 6)
            else: i += 1

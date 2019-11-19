class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        i = len(num1) - 1
        j = len(num2) - 1
        res = ""
        while i >= 0 or j >= 0:
            if i >= 0:
                carry += int(num1[i])
            if j >= 0:
                carry += int(num2[j])
            res += str(carry % 10)
            carry //= 10
            i -= 1
            j -= 1
        if carry != 0:
            res += str(carry)
        return res[::-1]
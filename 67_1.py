class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            if i >= 0:
                carry += int(a[i])
            if j >= 0:
                carry += int(b[j])
            res += str(carry % 2)
            carry = carry // 2
            i -= 1
            j -= 1
        if carry == 1:
            res += "1"
        return res[::-1]
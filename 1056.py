class Solution:
    def confusingNumber(self, N: int) -> bool:
        num = ""
        N = str(N)
        for i in range(len(N) - 1, -1 ,-1):
            if N[i] in {2,3,4,5,7}: return False
            if N[i] == "6": num += "9"
            elif N[i] == "9": num += "6"
            else: num += N[i]
        return not num == N
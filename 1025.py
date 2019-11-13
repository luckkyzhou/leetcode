class Solution:
    def divisorGame(self, N: int) -> bool:
        if N & 1 == 1: return False
        else: return True
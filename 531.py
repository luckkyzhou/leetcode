from typing import List

class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m = len(picture)
        n = len(picture[0])
        def isOnlyPixel(picture, row):
            count = 0
            for BW in picture[row]:
                if BW == 'B':
                    count += 1
            if count > 1: return False
            else: return True
        transposePicture = [T for T in zip(*picture)]
        res = 0
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B' and isOnlyPixel(picture, i) and isOnlyPixel(transposePicture, j):
                    res += 1
        return res
from typing import List
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        area = 0
        temp = set()
        for i in points:
            for j in temp:
                if (i[0],j[1]) in temp and (j[0],i[1]) in temp:
                    if not area: area = abs(i[0] - j[0]) * abs(i[1] - j[1])
                    else: area = min(area, abs(i[0] - j[0]) * abs(i[1] - j[1]))
            temp.add((i[0],i[1]))
        return area
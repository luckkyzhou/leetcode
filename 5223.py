# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        queens.sort()

        flag = False
        for x in range(1, 8):
            for i in range(len(queens)):
                if queens[i][1] == king[1] and queens[i][0] == king[0] + x:
                    res.append(queens[i])
                    flag = True
                    break
            if flag:
                break

        flag = False
        for x in range(1, 8):
            for i in range(len(queens)):
                if queens[i][1] == king[1] and queens[i][0] == king[0] - x:
                    res.append(queens[i])
                    flag = True
                    break
            if flag:
                break

        flag = False
        for x in range(1, 8):
            for i in range(len(queens)):
                if queens[i][0] == king[0] and queens[i][1] == king[1] + x:
                    res.append(queens[i])
                    flag = True
                    break
            if flag:
                break

        flag = False
        for x in range(1, 8):
            for i in range(len(queens)):
                if queens[i][0] == king[0] and queens[i][1] == king[1] - x:
                    res.append(queens[i])
                    flag = True
                    break
            if flag:
                break

        flag = False
        for x in range(1, 8):
            for i in range(len(queens)):
                if queens[i][0] == king[0] + x and queens[i][1] == king[1] - x:
                    res.append(queens[i])
                    flag = True
                    break
            if flag:
                break

        flag = False
        for x in range(1, 8):
            for i in range(len(queens)):
                if queens[i][0] == king[0] - x and queens[i][1] == king[1] + x:
                    res.append(queens[i])
                    flag = True
                    break
            if flag:
                break

        flag = False
        for x in range(1, 8):
            for i in range(len(queens)):
                if queens[i][0] == king[0] + x and queens[i][1] == king[1] + x:
                    res.append(queens[i])
                    flag = True
                    break
            if flag:
                break

        flag = False
        for x in range(1, 8):
            for i in range(len(queens)):
                if queens[i][0] == king[0] - x and queens[i][1] == king[1] - x:
                    res.append(queens[i])
                    flag = True
                    break
            if flag:
                break
        return res

if __name__ == '__main__':
    solution = Solution()
    queens = [[0,1],[1,0],[4,0],[0,4],[2,4],[3,3],[4,4],[1,1],[0,0]]
    king = [2,2]
    res = solution.queensAttacktheKing(queens,king)
    print(res)
# -*- coding: utf-8 -*-
from typing import List

'''
利用一个 two bits 的状态机来记录细胞状态, 第一位表示
下一状态, 第二位表示当前状态:
        00: dead (next state) <- dead (current state)
        01: dead (next state) <- live (current state) 
        10: live (next state) <- dead (current state)
        11: live (next state) <- live (current state) 
最后右移一位即为最终状态
'''
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        if len(board) == 0: return
        for i in range(len(board)):
            for j in range(len(board[0])):
                lives = self.countLives(board, i, j)
                if board[i][j] & 1 == 1:
                    if lives == 2 or lives == 3: board[i][j] = 3
                else:
                    if lives == 3: board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = board[i][j] >> 1

    def countLives(self, board: List[List[int]], i: int, j: int) -> int:
        count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for direction in directions:
            x = i + direction[0]
            y = j + direction[1]
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] & 1:
                count += 1
        return count

if __name__ == '__main__':
    solution = Solution()
    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    print(board)
    solution.gameOfLife(board)
    print(board)
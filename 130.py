# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        if not board or m == 0:
            return
        n = len(board[0])

        for i in range(m):
            self.DFS(board, i, 0)
            self.DFS(board, i, n - 1)
        for j in range(n):
            self.DFS(board, 0, j)
            self.DFS(board, m - 1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '-':
                    board[i][j] = 'O'
        return

    def DFS(self, board: List[List[str]], i: int, j: int):
        m = len(board)
        n = len(board[0])
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != 'O':
            return
        board[i][j] = '-'
        self.DFS(board, i - 1, j)
        self.DFS(board, i + 1, j)
        self.DFS(board, i, j - 1)
        self.DFS(board, i, j + 1)
        return

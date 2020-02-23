class Solution(object):
    def candyCrush(self, board):
        row = len(board)
        col = len(board[0])
        sameBoard = [[False for _ in range(col)] for _ in range(row)]
        todo = False

        for i in range(row):
            for j in range(col - 2):
                if board[i][j] == board[i][j + 1] == board[i][j + 2] != 0:
                    sameBoard[i][j] = sameBoard[i][j + 1] = sameBoard[i][j + 2] = True
                    todo = True

        for j in range(col):
            for i in range(row - 2):
                if board[i][j] == board[i + 1][j] == board[i + 2][j] != 0:
                    sameBoard[i][j] = sameBoard[i + 1][j] = sameBoard[i + 2][j] = True
                    todo = True

        for j in range(col):
            stack = []
            for i in range(row):
                if not sameBoard[i][j]: stack.append(board[i][j])
            for i in range(row - 1, -1, -1):
                if stack: board[i][j] = stack.pop()
                else: board[i][j] = 0
        return self.candyCrush(board) if todo else board
class TicTacToe:
    def __init__(self, n: int):
        # 定义二维矩阵，行用来存储player，列存储棋盘上行列对角线棋子状况
        self.n = n
        self.rows = [[0 for _ in range(n)] for _ in range(2)]
        self.cols = [[0 for _ in range(n)] for _ in range(2)]
        self.angles = [[0 for _ in range(2)] for _ in range(2)]

    def move(self, row: int, col: int, player: int) -> int:
        self.rows[player - 1][row] += 1
        self.cols[player - 1][col] += 1
        if row == col:
            self.angles[player - 1][0] += 1
        if row + col == self.n - 1:
            self.angles[player - 1][1] += 1

        if max(self.rows[player - 1][row], self.cols[player - 1][col], max(self.angles[player - 1])) == self.n:
            return player
        return 0
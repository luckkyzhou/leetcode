from typing import List

class Solution:
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    def DFS(self, grid, i, j, marked):
        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            while 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] != 'w':
                marked[new_i][new_j] = True
                new_i += direction[0]
                new_j += direction[1]

    def museumSecurity(self):
        size = input()
        m, n = size.split(' ')
        m, n = int(m), int(n)
        grid = [['-' for _ in range(n)] for _ in range(m)]
        marked = [[False for _ in range(n)] for _ in range(m)]

        GW = []
        while True:
            try:
                temp = input()
                GW.append(temp)
            except EOFError:
                break

        for coor in GW:
            x, y, s = coor.split(' ')
            x, y = int(x), int(y)
            grid[x][y] = s
            marked[x][y] = True

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'g':
                    self.DFS(grid, i, j, marked)

        res = []
        for i in range(m):
            for j in range(n):
                if marked[i][j] == False:
                    res.append([i, j])
        if len(res) == 0: print('true')
        else:
            print('false')
            for r in res:
                print(str(r[0]) + ' ' + str(r[1]))

if __name__ == '__main__':
    solution = Solution()
    solution.museumSecurity()
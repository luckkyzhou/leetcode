class Solution:
    def shortestDistance(self, grid):
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        queue = []
        res = 0

        for i in range(m):
            for j in range(n):
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    curX, curY = queue.pop(0)
                    if grid[curX][curY] == 9:
                        return res
                    for direction in directions:
                        newX = curX + direction[0]
                        newY = curY + direction[1]
                        if 0 <= newX < m and 0 <= newY < n and not visited[newX][newY] and grid[newX][newY] != 0:
                            visited[newX][newY] = True
                            queue.append((newX, newY))
                    res += 1
        return -1

if __name__ == '__main__':
    solution = Solution()
    res = solution.shortestDistance([[1,0,0],[1,0,0],[1,9,0]])
    print(res)
class Robot:
    def move(self):
        pass
    def turnLeft(self):
        pass
    def turnRight(self):
        pass
    def clean(self):
        pass


class Solution:
    def cleanRoom (self, robot):
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()

        def goBack ():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def DFS (cell, d):
            visited.add(cell)
            robot.clean()
            for i in range(4):
                new_d = (d + i) % 4
                new_cell = (cell[0] + directions[new_d][0], cell[1] + directions[new_d][1])

                if not new_cell in visited and robot.move():
                    DFS(new_cell, new_d)
                    goBack()
                robot.turnRight()

        DFS((0, 0), 0)
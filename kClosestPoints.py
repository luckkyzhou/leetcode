class Solution:
    def kClosest(self, points, origin, k):
        points.sort(key=lambda x: ((x[0] - origin[0]) ** 2 + (x[1] - origin[1]) ** 2, x[0], x[1]))
        res = []
        for i in range(k):
            res.append(points[i])
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.kClosest([(1,1),(2,2),(3,4),(1,3)],(3,5),2)
    print(res)
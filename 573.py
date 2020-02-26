class Solution(object):
    def minDistance(self, height, width, tree, squirrel, nuts):
        """
        :type height: int
        :type width: int
        :type tree: List[int]
        :type squirrel: List[int]
        :type nuts: List[List[int]]
        :rtype: int
        """
        res = 0
        diff = -2**31

        for nut in nuts:
            nutToTree = abs(nut[0] - tree[0]) + abs(nut[1] - tree[1])
            nutToSquirrel = abs(nut[0] - squirrel[0]) + abs(nut[1] - squirrel[1])
            diff = max(diff, nutToTree - nutToSquirrel)
            res += 2 * nutToTree
        res -= diff
        return res
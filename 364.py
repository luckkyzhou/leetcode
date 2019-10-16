from typing import List

class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        res = 0
        depth = self.findDepth(nestedList)
        for num in nestedList:
            res += self.sumDFS(num, depth)
        return res

    def sumDFS(self, num: NestedInteger, level):
        if num.isInteger(): return level * num.getInteger()
        res = 0
        for a in num.getList():
            res += self.sumDFS(a, level - 1)
        return res

    def findDepth(self, num: NestedInteger):
        res = 1
        for a in num:
            if not a.isInteger():
                res = max(res, self.findDepth(a.getList()) + 1)
        return res



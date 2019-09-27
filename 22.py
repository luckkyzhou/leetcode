# -*- coding: utf-8 -*-
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        res = []
        res.append([None])
        res.append(['()'])
        for i in range(2, n + 1):
            n_cur = []
            for j in range(i):
                cur_list1 = res[j]
                cur_list2 = res[i - 1 - j]
                for p in cur_list1:
                    for q in cur_list2:
                        if p == None: p = ''
                        if q == None: q = ''
                        cur = '(' + p + ')' + q
                        n_cur.append(cur)
            res.append(n_cur)
        return res[n]


if __name__ == '__main__':
    solution = Solution()
    res = solution.generateParenthesis(1)
    print(res)
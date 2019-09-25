# -*- coding: utf-8 -*-

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = 10000
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
        return maxprofit
if __name__ == '__main__':
    solution = Solution()
    res = solution.maxProfit([7, 1, 5, 3, 6, 4])
    print(res)
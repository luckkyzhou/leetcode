from typing import List
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        length = len(price)
        def shopping(special, needs):
            if not sum(needs): return 0

            special = list(filter(lambda x: all(x[i] <= needs[i] for i in range(length)), special))
            if not special:
                return sum(needs[i] * price[i] for i in range(length))
            res = []
            for pack in special:
                res.append(pack[-1] + shopping(special, [needs[i] - pack[i] for i in range(length)]))
            return min(res)
        special = list(filter(lambda x: x[-1] < sum(x[i] * price[i] for i in range(length)), special))
        return shopping(special, needs)

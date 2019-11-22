from typing import List
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        res = 0
        count = [0] * 121
        for i in range(len(ages)):
            count[ages[i]] += 1

        for i in range(15, len(count)):
            for j in range(i, len(count)):
                if i <= 0.5 * j + 7: break
                else:
                    if i == j: res += count[i] * (count[i] - 1)
                    else: res += count[i] * count[j]
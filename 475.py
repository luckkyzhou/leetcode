class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        res = []
        heaters.sort()

        for house in houses:
            left = 0
            right = len(heaters)
            while left < right:
                mid = left + (right - left) // 2
                if heaters[mid] <= house:
                    left = mid + 1
                elif heaters[mid] > house:
                    right = mid

            if heaters[left] == house:
                res.append(0)
            elif left == len(heaters) - 1:
                res.append(house - heaters[left])
            else:
                res.append(min(abs(heaters[left] - house), heaters[left + 1] - house))

        return max(res)
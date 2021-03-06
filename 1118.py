class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        hashmap = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        if (Y % 4 == 0 and Y % 100 != 0) or Y % 400 == 0:
            if M == 2: return 29
        return hashmap[M]
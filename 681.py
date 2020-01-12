import itertools
class Solution:
    def nextClosestTime(self, time: str) -> str:
        timeDigit = []
        for i in range(len(time)):
            if time[i] != ":":
                timeDigit.append(time[i])
        if timeDigit[0] == timeDigit[1] == timeDigit[2] == timeDigit[3]: return time
        times = list(itertools.product(timeDigit, repeat=4))

        count = 99999
        standard = int(time[:2]) * 60 + int(time[3:])
        for t in times:
            hour = str(t[0] + t[1])
            minute = str(t[2] + t[3])
            if int(hour) >= 24 or int(minute) >= 60: continue
            timeRes = hour + ":" + minute
            if timeRes == time:
                continue
            temp = int(timeRes[:2]) * 60 + int(timeRes[3:])
            if temp < standard:
                if 24 * 60 - standard + temp < count:
                    count = 24 * 60 - standard + temp
                    res = timeRes
            else:
                if temp - standard < count:
                    count = temp - standard
                    res = timeRes
        return res

if __name__ == '__main__':
    solution = Solution()
    res = solution.nextClosestTime("23:59")
    print(res)
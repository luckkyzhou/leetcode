# -*- coding: utf-8 -*-

class Solution:
    res1 = ('', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')
    res2 = ('Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen')
    res3 = ('', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety')
    def find(self, num: int):
        if num < 10:
            res = self.res1[num]
        elif num < 20:
            res = self.res2[num - 10]
        elif num < 100:
            res = self.res3[num // 10] + ' ' + self.find(num % 10)
            if res[-1] == ' ':
                res = res[:-1]
        elif num < 1000:
            res = self.find(num // 100) + ' Hundred ' + self.find(num % 100)
            if res[-1] == ' ':
                res = res[:-1]
        elif num < 1000000:
            res = self.find(num // 1000) + ' Thousand ' + self.find(num % 1000)
            if res[-1] == ' ':
                res = res[:-1]
        elif num < 1000000000:
            res = self.find(num // 1000000) + ' Million ' + self.find(num % 1000000)
            if res[-1] == ' ':
                res = res[:-1]
        else:
            res = self.find(num // 1000000000) + ' Billion ' + self.find(num % 1000000000)
            if res[-1] == ' ':
                res = res[:-1]
        return res


    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        else:
            res = self.find(num)
            while res[-1] == ' ':
                res = res[:-1]
        return res



if __name__ == '__main__':
    solution = Solution()
    res = solution.numberToWords(50868)

    print(res)
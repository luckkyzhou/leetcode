class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            digit = ""
            while j < len(abbr) and abbr[j].isdigit():
                digit += abbr[j]
                j += 1
            if digit:
                if digit[0] == "0": return False
                i += int(digit)
            else:
                if word[i] != abbr[j]: return False
                i += 1
                j += 1
        return i == len(word) and j == len(abbr)

if __name__ == '__main__':
    solution = Solution()
    res = solution.validWordAbbreviation("apple", "a2le")
    print(res)
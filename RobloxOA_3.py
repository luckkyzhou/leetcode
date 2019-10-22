def palindrome(s):
    res = []
    def count(s: str, start: int, end: int, res):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            res.append(s[start:end+1])
            start -= 1
            end += 1
        return res
    for i in range(len(s)):
        res = count(s, i, i, res)
        res = count(s, i, i + 1, res)
    hashmap = {}
    res1 = hashmap.fromkeys(res).keys()
    return len(res1)



if __name__ == '__main__':
    res = palindrome('aa')
    print(res)
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        hashmap = {"6":"9","9":"6","8":"8","1":"1","0":"0"}
        res = ""
        for n in num:
            if n in hashmap: res += hashmap[n]
            else: return False
        return res[::-1] == num
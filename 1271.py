class Solution:
    def toHexspeak(self, num: str) -> str:
        res = hex(int(num))
        res = res[2:].upper()
        res = res.replace("0", "O")
        res = res.replace("1", "I")
        check = {"A", "B", "C", "D", "E", "F", "I", "O"}
        for r in res:
            if r not in check: return "ERROR"
        return res
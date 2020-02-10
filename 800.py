class Solution:
    def similarRGB(self, color: str) -> str:
        return "#" + "".join(map(lambda x: hex((int(x, 16) + 8) // 17)[2:] * 2, (color[i:i+2] for i in range(1,7,2))))
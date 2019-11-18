from typing import List
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # 构建有向图
        hashmap = {}
        for i in range(len(words) - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    hashmap.setdefault(words[i][j], []).append(words[i + 1][j])
                    break

        # 设定入度数组，没出现过的为-1，出现过的字符出度为0
        # 在value中出现过的字符出度循环+=1
        degrees = [-1] * 26
        for word in words:
            for char in word:
                degrees[ord(char) - 97] = 0
        for value in hashmap.values():
            for char in value:
                degrees[ord(char) - 97] += 1

        # 记录节点数，并设定出度为0的list
        count = 0
        degree_0 = set()
        for i in range(26):
            if degrees[i] != -1:
                count += 1
            if degrees[i] == 0:
                degree_0.add(chr(97 + i))

        # 循环pop，直到出度为0的数组为空
        res = []
        while degree_0:
            cur = degree_0.pop()
            res.append(cur)
            if cur in hashmap.keys():
                for char in hashmap[cur]:
                    degrees[ord(char) - 97] -= 1
                    if degrees[ord(char) - 97] == 0:
                        degree_0.add(char)

        # 判断是否有环
        if len(res) != count:
            return ""
        else:
            return "".join(res)

if __name__ == '__main__':
    solution = Solution()
    #res = solution.alienOrder(["za","zb","ca","cb"])
    res = solution.alienOrder(["a","b","ca","cc"])
    print(res)
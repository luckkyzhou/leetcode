from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 构建字典树
        trie = {}
        for word in words:
            node = trie
            for char in word:
                if char in node.keys():
                    node = node[char]
                else:
                    node[char] = {}
                    node = node[char]
            node["end"] = True

        res = []
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def DFS(i, j, node, curStr):
            char = board[i][j]
            if char not in node:
                return
            node = node[char]
            # 改变end键值是为了去重，若一个单词搜索完，那么end=False
            if "end" in node and node["end"]:
                res.append(curStr + char)
                node["end"] = False
            board[i][j] = "#"
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]) and board[new_i][new_j] != "#":
                    DFS(new_i, new_j, node, curStr + char)
            # 单个位置开头的单词已经搜索完，复原
            board[i][j] = char

        for i in range(len(board)):
            for j in range(len(board[0])):
                DFS(i, j, trie, "")
        return res
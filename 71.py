class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for pa in path.split("/"):
            if pa not in ["",".",".."]:
                stack.append(pa)
            elif pa == ".." and stack:
                stack.pop()
        return "/" + "/".join(stack)
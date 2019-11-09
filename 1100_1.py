class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        visited = [0] * 26
        queue = []
        count = 0

        for i in range(len(S)):
            queue.append(S[i])
            visited[ord(S[i]) - 97] += 1
            if len(queue) == K:
                temp = max(visited)
                if temp == 1:
                    count += 1
                visited[ord(queue[0]) - 97] -= 1
                queue.pop(0)
        return count

if __name__ == '__main__':
    solution = Solution()
    res = solution.numKLenSubstrNoRepeats("havefunonleetcode",5)
    print(res)
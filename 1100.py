class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        queue = []
        count = 0
        for i in range(len(S)):
            queue.append(S[i])
            if queue and len(queue) == K:
                if len(set(queue)) == len(queue):
                    count += 1
                queue.pop(0)
        return count

if __name__ == '__main__':
    solution = Solution()
    res = solution.numKLenSubstrNoRepeats("havefunonleetcode",5)
    print(res)
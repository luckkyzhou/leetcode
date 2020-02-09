class Solution:
    def countAndSay(self, n: int) -> str:
        arr = ["1"]
        for i in range(n - 1):
            tmp = ""
            cnt = 1
            j = 0
            while j < len(arr[i]):
                while j < len(arr[i]) and arr[i][j] == arr[i][j + 1]:
                    cnt += 1
                    j += 1
                tmp += str(cnt) + arr[i][j]
            arr.append(tmp)
        return arr[n - 1]
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        bucketS = [0] * 10
        bucketG = [0] * 10

        for i in range(len(secret)):
            if secret[i] == guess[i]: bulls += 1
            bucketS[int(secret[i])] += 1
            bucketG[int(guess[i])] += 1
        for i in range(10):
            if bucketS[i] > 0 and bucketG[i] > 0: cows += min(bucketS[i], bucketG[i])
        cows -= bulls

        return str(bulls) + "A" + str(cows) + "B"
# Problem ID: 299
# Title: Bulls and Cows
# Runtime: 7 ms

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s,g = [0]*10 , [0]*10
        n = len(secret)
        bulls = 0
        for i in range(n):
            if secret[i] == guess[i]:
                bulls+=1
            s[int(secret[i])]+=1
            g[int(guess[i])]+=1
        cows = -bulls
        for i in range(10):
            cows+=min(s[i],g[i])
        return str(bulls)+"A"+str(cows)+"B"
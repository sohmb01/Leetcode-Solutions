# Problem ID: 464
# Title: Can I Win
# Runtime: 2243 ms

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        if maxChoosableInteger >= desiredTotal:
            return True
        if sum(range(1,maxChoosableInteger+1)) < desiredTotal:
            return False

        memo = {}
        def backTrack(choices, total):
            state = tuple(choices)
            if state in memo:
                return memo[state]
            if choices[-1] >= total:
                memo[state] = True
                return True
            for i in range(len(choices)):
                if not backTrack(choices[:i]+choices[i+1:],total - choices[i]):
                    memo[state] = True
                    return True
            memo[state] = False
            return False
        return backTrack(list(range(1,maxChoosableInteger+1)),desiredTotal)
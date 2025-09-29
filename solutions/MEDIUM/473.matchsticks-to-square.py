# Problem ID: 473
# Title: Matchsticks to Square
# Runtime: 3919 ms

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        if s%4 !=0 :
            return False
        
        length = s // 4
        visit = set()
        sides = [0] * 4
        matchsticks.sort(reverse = True)
        
        def check(i):
            if i == len(matchsticks):
                return True
            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j]+=matchsticks[i]
                    if check(i+1):
                        return True
                    sides[j]-=matchsticks[i]
            return False
        return check(0)
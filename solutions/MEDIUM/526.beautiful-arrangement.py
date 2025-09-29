# Problem ID: 526
# Title: Beautiful Arrangement
# Runtime: 1139 ms

class Solution:
    def countArrangement(self, n: int) -> int:
        
        def backtrack(temp,l):
            if len(temp) == n:
                res[0]+=1
                return
            for num in range(1,n+1):
                if num not in temp and (num % l == 0 or l % num == 0):
                    temp.append(num)
                    backtrack(temp,l+1)
                    temp.pop()

        res = [0]
        backtrack([],1)
        return res[0]
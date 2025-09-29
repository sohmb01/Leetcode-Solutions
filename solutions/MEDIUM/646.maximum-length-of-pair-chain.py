# Problem ID: 646
# Title: Maximum Length of Pair Chain
# Runtime: 11 ms

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x:x[1])
        prev = pairs[0]
        res = 1
        for curr in pairs[1:]:
            if curr[0] > prev[1]:
                res+=1
                prev = curr
        return res
        

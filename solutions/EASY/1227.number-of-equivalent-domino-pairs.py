# Problem ID: 1227
# Title: Number of Equivalent Domino Pairs
# Runtime: 7 ms

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = 0
        freq = {}
        for i in range(len(dominoes)):
            dominoes[i].sort()
            a,b = dominoes[i]
            if (a,b) not in freq:
                freq[(a,b)] = 1
            else:
                freq[(a,b)]+=1
        for _, value in freq.items():
            if value > 1:
                res += value*(value-1)//2
        return res
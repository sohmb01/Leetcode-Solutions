# Problem ID: 2529
# Title: Range Product Queries of Powers
# Runtime: 87 ms

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        mod = 10**9 + 7
        x = 0
        while n:
            if n%2:
                powers.append(x)
            x+=1
            n//=2

        # making powers a prefix array
        for i in range(1,len(powers)):
            powers[i] += powers[i-1]
        
        res = []
        for start, end in queries:
            if start == 0:
                x = powers[end]
            else:
                x = powers[end]-powers[start-1]
            res.append(2**x % mod)
        return res

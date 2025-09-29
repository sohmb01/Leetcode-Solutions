# Problem ID: 2107
# Title: Find Unique Binary String
# Runtime: 0 ms

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        st= set(nums)
        def backtrack(i, l):
            if i == n:
                s = "".join(l)
                return None if s in st else s
            
            res = backtrack(i+1, l)
            if res:
                return res
            l[i] = "1"
            res = backtrack(i+1, l)
            if res:
                return res
        return backtrack(0,['0' for _ in range(n)])
                

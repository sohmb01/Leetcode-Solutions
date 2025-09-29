# Problem ID: 1426
# Title: Find N Unique Integers Sum up to Zero
# Runtime: 0 ms

class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [ _ for _ in range(1,n)] + [-((n-1)*n//2)]
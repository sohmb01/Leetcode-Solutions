# Problem ID: 2456
# Title: Construct Smallest Number From DI String
# Runtime: 0 ms

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        res, st = [],[]
        for i in range(n+1):
            st.append(i+1)
            while st and (i == n or pattern[i] == 'I'):
                res.append(str(st.pop()))
        return "".join(res)

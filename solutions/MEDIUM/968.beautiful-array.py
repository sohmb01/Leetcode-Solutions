# Problem ID: 968
# Title: Beautiful Array
# Runtime: 0 ms

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        ans = [1]
        while len(ans) < n:
            ans = [(2*x - 1) for x in ans] + [2*x for x in ans]
        return [x for x in ans if x<=n]

        
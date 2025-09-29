# Problem ID: 3459
# Title: Find the Minimum Area to Cover All Ones II
# Runtime: 8201 ms

class Solution:
    def minimumSum(self, A: List[int]) -> int:
        def f(s, k):
            if not s:
                return 0
            left, top, right, bottom = inf, inf, 0, 0
            for i, j in s:
                left = min(left, j)
                top = min(top, i)
                right = max(right, j)
                bottom = max(bottom, i)
            res = (bottom - top + 1) * (right - left + 1)
            if k == 1:
                return res

            # Split Horizontally
            for x in range(top, bottom):
                s2 = set((i, j) for i, j in s if i <= x)
                res = min(res, f(s2, 1) + f(s - s2, k - 1), f(s2, k - 1) + f(s - s2, 1))

            # Split Vertically
            for y in range(left, right):
                s2 = set((i, j) for i, j in s if j <= y)
                res = min(res, f(s2, 1) + f(s - s2, k - 1), f(s2, k - 1) + f(s - s2, 1))

            return res

        m, n = len(A), len(A[0])
        s = set((i, j) for i in range(m) for j in range(n) if A[i][j])
        return f(s, 3)
        
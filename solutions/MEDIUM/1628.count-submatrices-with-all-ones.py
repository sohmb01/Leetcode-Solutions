# Problem ID: 1628
# Title: Count Submatrices With All Ones
# Runtime: 31 ms

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows,cols = len(mat), len(mat[0])
        ans = 0

        for i, h in enumerate(mat):
            st = []
            cnt = [0] * cols
            for j in range(cols):
                if i > 0 and h[j]:
                    h[j]+=mat[i-1][j]
                while st and h[st[-1]] > h[j]:
                    st.pop()
                left = st[-1] if st else -1
                cnt[j] = h[j] * (j-left)
                if st:
                    cnt[j]+=cnt[left]
                ans+=cnt[j]
                st.append(j)
        return ans

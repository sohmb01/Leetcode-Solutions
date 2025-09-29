# Problem ID: 3629
# Title: Total Characters in String After Transformations I
# Runtime: 2173 ms

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        
        mod = 10 ** 9 + 7
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')]+=1
        for move in range(t):
            temp = [0] * 26
            temp[0] = cnt[25]
            temp[1] = (cnt[25]+cnt[0])%mod
            for i in range(2,26):
                temp[i] = cnt[i-1]
            cnt = temp
        ans = sum(cnt)%mod

        return ans
        
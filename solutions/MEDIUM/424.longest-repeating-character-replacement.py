# Problem ID: 424
# Title: Longest Repeating Character Replacement
# Runtime: 111 ms

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = [0]*26
        l,r = 0,0
        n = len(s)
        ans = 0
        while r < n:
            mp[ord(s[r])-ord('A')] += 1

            while r-l+1 - max(mp)>k:
                mp[ord(s[l])-ord('A')] -= 1
                l+=1
            
            ans = max(ans,r-l+1)
            r+=1
        return ans

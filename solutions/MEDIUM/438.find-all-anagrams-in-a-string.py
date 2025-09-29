# Problem ID: 438
# Title: Find All Anagrams in a String
# Runtime: 23 ms

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lp = len(p)
        if lp > len(s):
            return []
        ans = []
        freq, target= [0]*26, [0]*26
        for i in range(lp):
            target[ord(p[i])-ord('a')]+=1
            freq[ord(s[i])-ord('a')]+=1
        if freq == target:
            ans.append(0)
        for i in range(lp,len(s)):
            idx = ord(s[i-lp])-ord('a')
            freq[idx]-=1
            idx = ord(s[i])-ord('a')
            freq[idx]+=1
            if freq == target:
                ans.append(i-lp+1)

        return ans

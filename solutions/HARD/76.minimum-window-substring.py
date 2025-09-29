# Problem ID: 76
# Title: Minimum Window Substring
# Runtime: 124 ms

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target, window = {},{}
        curr, targetCnt = 0,0
        for char in t:
            if char in target:
                target[char] +=1
            else:
                target[char] = 1
                targetCnt +=1
                window[char] = 0
        l,r=0,0
        minLength,ans,n = len(s),"",len(s)
        
        while r<n:
            if s[r] in window:
                window[s[r]] += 1
                if window[s[r]] == target[s[r]]:
                    curr+=1

            while curr == targetCnt:
                if minLength >= r-l+1:
                    minLength = r-l+1
                    ans = s[l:r+1]
                if s[l] in window:
                    window[s[l]]-=1
                    if window[s[l]] < target[s[l]]:
                        curr-=1
                l+=1

            r+=1
        return ans
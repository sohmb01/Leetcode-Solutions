# Problem ID: 3
# Title: Longest Substring Without Repeating Characters
# Runtime: 18 ms

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = len(s)
        mp = [-1] * 128
        dp = [1] * l
        ans = 1
        mp[ord(s[0])] = 0
        for i in range (1,l):
            if mp[ord(s[i])] == -1:
                dp[i] = dp[i-1]+1
                # ans = max(ans,dp[i])
            else:
                if i-mp[ord(s[i])]>dp[i-1]:
                    dp[i] = dp[i-1]+1
                    # ans = max(ans,dp[i])
                else:
                    dp[i] = i-mp[ord(s[i])]
            ans = max(ans,dp[i]) 
            mp[ord(s[i])] = i

        return ans
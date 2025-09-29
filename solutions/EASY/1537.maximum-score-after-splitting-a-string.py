# Problem ID: 1537
# Title: Maximum Score After Splitting a String
# Runtime: 0 ms

class Solution:
    def maxScore(self, s: str) -> int:
        ones,zeroes,ans = 0,0,-inf
        for i in range(len(s)-1):
            if s[i]=="1":
                ones+=1
            else:
                zeroes+=1
            ans = max(ans,zeroes-ones)
        if s[-1]=="1":
            ones+=1
        return ans+ones
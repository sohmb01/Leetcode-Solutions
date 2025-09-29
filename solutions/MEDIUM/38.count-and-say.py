# Problem ID: 38
# Title: Count and Say
# Runtime: 52 ms

class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        
        s=self.countAndSay(n-1)
        ans=""
        count=1
        i=1
        while i<len(s)+1:
            if i<len(s) and s[i]==s[i-1]:
                count+=1
            else:
                ans=ans+str(count)+str(s[i-1])
                count=1
            i+=1
                
        return ans
                
        
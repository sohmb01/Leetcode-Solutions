# Problem ID: 151
# Title: Reverse Words in a String
# Runtime: 0 ms

class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split(" ")
        ans = ""
        for i in range(len(l)-1,-1,-1):
            k = l[i].strip()
            if k:
                ans+= k+" "
        return ans[:-1]
        

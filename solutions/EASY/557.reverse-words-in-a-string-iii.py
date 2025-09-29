# Problem ID: 557
# Title: Reverse Words in a String III
# Runtime: 64 ms

class Solution:
    def reverseWords(self, s: str) -> str:
        l=[]
        word=""
        for char in s:
            if char == ' ':
                l.append(word[::][::-1])
                word=""
                continue
            word+=char
        l.append(word[::][::-1])
        ans=""
        for w in l:
            ans+=w
            ans+=" "
        
        return ans[:-1]
            
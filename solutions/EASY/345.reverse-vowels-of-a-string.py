# Problem ID: 345
# Title: Reverse Vowels of a String
# Runtime: 52 ms

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels={'a','e','i','o','u','A','E','I','O','U'}
        seq=[]
        for i in s:
            if i in vowels:
                seq.append(i)
        seq=seq[::-1]
        if len(seq)==0:
            return s
        p=0
        ans=""
        for i in s:
            if i in vowels:
                ans+=seq[p]
                p+=1
            else:
                ans+=i
                
        return ans
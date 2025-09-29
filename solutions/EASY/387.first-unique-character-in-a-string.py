# Problem ID: 387
# Title: First Unique Character in a String
# Runtime: 252 ms

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count=[0]*26
        indx = lambda ch : ord(ch) % ord('a') 
        for i in s:
            count[indx(i)]+=1
        for i in range(len(s)):
            if count[indx(s[i])]==1:
                return i
        return -1
        
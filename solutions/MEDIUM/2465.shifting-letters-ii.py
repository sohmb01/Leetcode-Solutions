# Problem ID: 2465
# Title: Shifting Letters II
# Runtime: 63 ms

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0]*(n+1)
        for shift in shifts:
            start,end,direction = shift[0],shift[1],shift[2]
            if direction:
                prefix[start]+=1
                prefix[end+1]-=1
            else:
                prefix[start]-=1
                prefix[end+1]+=1
        print(prefix)
        ans = ""
        currShift = 0
        for i in range(len(s)):
            currShift += prefix[i]
            ans += chr(((ord(s[i])-ord('a')) + (currShift%26))%26 + ord('a'))
        return ans
                
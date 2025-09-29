# Problem ID: 1529
# Title: Max Difference You Can Get From Changing an Integer
# Runtime: 0 ms

class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        i = 0
        while i < len(s) and s[i]=="9":
            i+=1
        if i<len(s):
            a = int(s.replace(s[i],"9"))
        else:
            a = num
        i = 0
        while i < len(s) and (s[i]=="1" or s[i]=="0"):
            i+=1
        if i<len(s) and s[0]=="1":
            b = int(s.replace(s[i],"0"))
        elif i<len(s) and s[0]!= "1":
            b = int(s.replace(s[0],"1"))
        else:
            b = num
        print(a)
        print(b)
        return a-b

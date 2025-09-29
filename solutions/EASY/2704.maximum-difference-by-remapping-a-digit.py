# Problem ID: 2704
# Title: Maximum Difference by Remapping a Digit
# Runtime: 0 ms

class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        
        def getNum(original, new):
            num = ""
            for c in s:
                if c == original:
                    num+=new
                else:
                    num+=c
            return int(num)
            
        i = 0
        while i<len(s) and s[i]== "9":
            i+=1
        if i<len(s):
            d = s[i]
        else:
            d = "9"
        return getNum(d, "9") - getNum(s[0],"0")
    
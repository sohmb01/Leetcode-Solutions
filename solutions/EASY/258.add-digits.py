# Problem ID: 258
# Title: Add Digits
# Runtime: 32 ms

class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        ans=0
        while num:
            ans+=num%10
            num=num//10
        return self.addDigits(ans)
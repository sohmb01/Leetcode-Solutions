# Problem ID: 804
# Title: Rotated Digits
# Runtime: 15 ms

class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = set(["2","5","6","9"])
        invalid = {"3","4","7"}
        cnt = 0
        for num in range(1,n+1):
            isGood = False
            for c in str(num):
                if c in invalid:
                    isGood = False
                    break
                if c in valid:
                    isGood = True
            if isGood:
                cnt+=1
        return cnt
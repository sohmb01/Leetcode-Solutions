# Problem ID: 1889
# Title: Check if Number is a Sum of Powers of Three
# Runtime: 0 ms

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        i = 0
        while 3**i < n:
            i+=1
        while i>=0:
            if n >= 3**i:
                n-= 3**i
            if n > 3**i:
                return False
            i-=1
            if n == 0:
                return True
        return False

        
        
        

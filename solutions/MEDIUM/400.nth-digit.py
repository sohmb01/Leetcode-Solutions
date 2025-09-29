# Problem ID: 400
# Title: Nth Digit
# Runtime: 0 ms

class Solution:
    def findNthDigit(self, n: int) -> int:
        if n<10:
            return n
        digits = 1
        totalDigits = 9
        while True:
            
            if totalDigits > n:
                break
            else:
                n-=totalDigits
            digits +=1
            totalDigits = (digits * 9 * (10**(digits-1)))
        
        num = (10**(digits-1) + n//digits) - 1 
        if n%digits:
            num+=1
        print (num)
        return int(str(num)[n%digits-1])

        







                
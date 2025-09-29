# Problem ID: 507
# Title: Perfect Number
# Runtime: 40 ms

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        i=2
        s=1
        j=num
        while i<j:
            if num%i==0:
                j=num//i
                s+=i
                s+=j
            j=num//i
            i+=1
            
            
        return s==num and s!=1
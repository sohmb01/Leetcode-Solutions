# Problem ID: 728
# Title: Self Dividing Numbers
# Runtime: 36 ms

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l=[]
        for i in range (left,right+1):
            if self.isTrue(i):
                l.append(i)
        return l
    
    def isTrue(self,num):
        k=num
        while k:
            if not k%10  or num % (k%10) !=0:
                return False
            k=k//10
        
        return True
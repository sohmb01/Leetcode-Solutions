# Problem ID: 204
# Title: Count Primes
# Runtime: 1216 ms

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        l=[]
        for i in range (0,n):
            l.append(0)
        i=2
        count=0
        while i<n:
            if l[i]==0:
                count+=1
                l[i]=1
                j=i
                while j<n:
                    l[j]=1
                    j+=i
            i+=1
        return count
# Problem ID: 2610
# Title: Closest Prime Numbers in Range
# Runtime: 2075 ms

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        nums = [True for i in range(right+1)]
        
        p = 2
        while p*p < right+1:

            if nums[p]:
                for i in range(p+p, right+1, p):
                    nums[i] = False
            p+=1
        nums[1] = False
        primes = []
        for i in range(left, right+1):
            if nums[i]:
                primes.append(i)
        if len(primes) < 2:
            return [-1,-1]
        diff = float('inf')
        for i in range(len(primes)-1):
            if primes[i+1] - primes[i] < diff:
                ans = [primes[i] , primes[i+1]]
                diff = primes[i+1] - primes[i]
        return ans
        
        
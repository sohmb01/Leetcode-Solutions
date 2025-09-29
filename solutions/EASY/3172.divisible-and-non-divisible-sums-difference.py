# Problem ID: 3172
# Title: Divisible and Non-divisible Sums Difference
# Runtime: 4 ms

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        res = 0
        for num in range(1,n+1):
            if num%m != 0:
                res+=num
            else:
                res-= num
        return res
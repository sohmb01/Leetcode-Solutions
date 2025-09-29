# Problem ID: 264
# Title: Ugly Number II
# Runtime: 51 ms

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        i2,i3,i5 = 0,0,0
        cnt = 1
        while cnt<n:
            n2 = 2 * dp[i2]
            n3 = 3 * dp[i3]
            n5 = 5 * dp[i5]

            nextUgly = min(n2,n3,n5)
            if n2 == nextUgly:
                i2+=1
            if n3 == nextUgly:
                i3+=1
            if n5 == nextUgly:
                i5+=1
            
            dp.append(nextUgly)
            cnt+=1
        return dp[-1]

        
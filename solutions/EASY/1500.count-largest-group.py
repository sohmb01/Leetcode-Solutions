# Problem ID: 1500
# Title: Count Largest Group
# Runtime: 19 ms

class Solution:
    def countLargestGroup(self, n: int) -> int:
        mp = [0]*37
        for num in range(1,n+1):
            s = 0
            while num:
                s += num%10
                num = num // 10
            mp[s] += 1
        maxFreq = max(mp)
        res = 0
        for freq in mp:
            if freq == maxFreq:
                res +=1

        return res
        
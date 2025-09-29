# Problem ID: 2802
# Title: Find the Punishment Number of an Integer
# Runtime: 918 ms

class Solution:
    def punishmentNumber(self, n: int) -> int:
        def isPunishmentNo(idx, s, num):
            if num < 0 :
                return False
            if idx == len(s):
                return num == 0
            for i in range(idx,len(s)):
                a = s[idx:i+1]
                if isPunishmentNo(i+1,s,num-int(a)):
                    return True
            return False

        ans = 0
        for num in range(1,n+1):
            if isPunishmentNo(0,str(num*num),num):
                ans += num * num
        return ans
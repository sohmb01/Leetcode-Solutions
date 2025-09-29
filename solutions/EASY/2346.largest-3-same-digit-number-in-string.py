# Problem ID: 2346
# Title: Largest 3-Same-Digit Number in String
# Runtime: 0 ms

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = 1
        last = num[0]
        n = len(num)
        curr = -1
        while i < n:
            l = 1
            while i<n and num[i] == last:
                i+=1
                l+=1
            if l >= 3:
                curr = max(curr, int(last))
            if i<n:
                last = num[i]
            i+=1

        return str(curr) * 3 if curr != -1 else ""



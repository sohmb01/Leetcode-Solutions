# Problem ID: 202
# Title: Happy Number
# Runtime: 0 ms

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited:
            visited.add(n)
            x = n
            n = 0
            while x:
                digit = x%10
                x = x//10
                n+=digit**2
            if n == 1:
                return True
        return False
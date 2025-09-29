# Problem ID: 2221
# Title: Check if a Parentheses String Can Be Valid
# Runtime: 57 ms

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        lockedStack, unlockedStack = [], []
        n = len(s)
        if n%2:
            return False
        for i in range(n):
            if locked[i] == "1":
                if s[i] == ")":
                    if len(lockedStack):
                        lockedStack.pop()
                    elif len(unlockedStack):
                        unlockedStack.pop()
                    else:
                        return False
                else:
                    lockedStack.append(i)
            else:
                unlockedStack.append(i)
 
        if len(lockedStack)==0:
            return True
        while lockedStack:
            par = lockedStack.pop()
            if unlockedStack and unlockedStack[-1] > par:
                unlockedStack.pop()
            else:
                return False
        return len(lockedStack)==0
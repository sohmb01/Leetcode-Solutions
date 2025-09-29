# Problem ID: 20
# Title: Valid Parentheses
# Runtime: 30 ms

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
                continue
            if stack[-1] == '(' and c == ')':
                stack.pop(-1)
            elif stack[-1] == '[' and c == ']':
                stack.pop(-1)
            elif stack[-1] == '{' and c == '}':
                stack.pop(-1)
            else:
                stack.append(c)
        print(stack)
        return not stack
            
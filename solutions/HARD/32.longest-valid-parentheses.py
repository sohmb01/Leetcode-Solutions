# Problem ID: 32
# Title: Longest Valid Parentheses
# Runtime: 7 ms

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        mxLength = 0
        for i,c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    mxLength = max(mxLength, i - stack[-1])
        return mxLength
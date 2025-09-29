# Problem ID: 886
# Title: Score of Parentheses
# Runtime: 0 ms

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                p = stack.pop()
                if p == "(":
                    temp = 1
                else:
                    temp = 0
                    while p != "(":
                        temp += p * 2
                        p = stack.pop()
                stack.append(temp)
        return sum(stack)
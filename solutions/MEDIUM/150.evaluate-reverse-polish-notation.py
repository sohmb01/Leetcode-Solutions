# Problem ID: 150
# Title: Evaluate Reverse Polish Notation
# Runtime: 2 ms

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        i = 0
        while i<len(tokens):
            token = tokens[i]
            if token in "+-/*":
                a = stack.pop()
                b = stack.pop()
                if token == "+":
                    token = a+b
                elif token == "-":
                    token = b-a
                elif token == "/":
                    token = int(b/a) 
                else:
                    token = a*b
            stack.append(int(token))
            i+=1
        return stack[0]
                
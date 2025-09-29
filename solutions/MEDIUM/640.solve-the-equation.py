# Problem ID: 640
# Title: Solve the Equation
# Runtime: 0 ms

class Solution:
    def solveEquation(self, equation: str) -> str:
        def parseStr(s):
            cnt,val = 0,0
            i, sign = 0, 1
            while i < len(s):
                if s[i] == "x":
                    cnt+= sign * 1
                elif s[i] == "+":
                    sign = 1
                elif s[i] == "-":
                    sign = -1
                else:
                    curr =0 
                    while i<len(s) and s[i].isnumeric():
                        curr = curr * 10 + int(s[i])
                        i+=1
                    if i<len(s) and s[i] == "x":
                        cnt+= sign * curr
                        i+=1
                    else:
                        val += sign * curr
                    i-=1
                i+=1
            
            return cnt, val

        lhs,rhs = equation.split("=")
        leftX,leftVal = parseStr(lhs)
        rightX,rightVal = parseStr(rhs)
        
        if leftX == rightX:
            if leftVal == rightVal:
                return "Infinite solutions"
            else:
                return "No solution"
        elif leftX < rightX:
            xCnt = rightX - leftX
            val = leftVal - rightVal
        else:
            xCnt = leftX - rightX 
            val = rightVal - leftVal
        res = val//xCnt
        return "x=" + str(res)

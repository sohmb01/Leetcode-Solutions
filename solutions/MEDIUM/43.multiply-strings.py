# Problem ID: 43
# Title: Multiply Strings
# Runtime: 67 ms

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1),len(num2)
        l = [0] * (m+n)
        if num1=="0" or num2 == "0":
            return "0"
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                product = int(num1[i])*int(num2[j])
                product+= l[i+j+1]
                l[i+j] += product//10
                l[i+j+1] = product%10
        l = [str(x) for x in l]
        ans = "".join(l)
        i = 0
        while ans[i]=="0":
            i+=1
        return ans[i:]
# Problem ID: 227
# Title: Basic Calculator II
# Runtime: 71 ms

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")
        n = len(s)
        st = []
        signs = set(['+','-','/','*'])
        lastSign,sign = "!","!"
        i = 0
        while i<n:
            num = 0
            while i<n and s[i] not in signs:
                num = num * 10 + int(s[i])
                i+=1
            if i<n:
                sign = s[i]
                i+=1
            if lastSign == "*":
                num *= st.pop() 
            elif lastSign == "/":
                div = st.pop()
                num = abs(div)//num
                if div<0:
                    num *= -1
                
            elif lastSign == "-":
                num *= -1
            else:
                pass
            st.append(num)
            lastSign = sign
            
        return sum(st)
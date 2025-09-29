# Problem ID: 394
# Title: Decode String
# Runtime: 0 ms

class Solution:
    def decodeString(self, s: str) -> str:
        ans = ""
        stack = [""]
        i = 0
        while i<len(s):
            if s[i] == ']':
                temp = ""
                while stack[-1]!='[':
                    temp = stack.pop() + temp
                stack.pop()
                num = ""
                while stack[-1].isnumeric():
                    num = stack.pop() + num
                stack.append(int(num)*temp)
            else:
                stack.append(s[i])
            i+=1
        for k in stack:
            ans+=k
        return ans

                
    
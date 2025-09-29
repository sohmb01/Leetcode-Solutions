# Problem ID: 8
# Title: String to Integer (atoi)
# Runtime: 0 ms

class Solution:
    def myAtoi(self, s: str) -> int:
        mn,mx = -pow(2,31),pow(2,31)-1
        i, n = 0 , len(s)
        k = ""
        flag = 0
        while i<n and s[i]==" ":
            i+=1
        if i<n and (s[i]=="-" or s[i]=="+"):
            if s[i]=="-":
                flag-=1
            i+=1

        while i<n and s[i].isdigit():
            k+=s[i]
            i+=1
        if not k:
            return 0
        if flag<0:
            ans = max(-int(k),mn)
        else:
            ans = min(int(k),mx)
        return ans
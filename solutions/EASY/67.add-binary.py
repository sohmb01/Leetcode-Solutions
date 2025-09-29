# Problem ID: 67
# Title: Add Binary
# Runtime: 36 ms

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la=len(a)
        lb=len(b)
        diff=abs(la-lb)
        st=""
        for i in range(diff):
            st+='0'
        if la>lb:
            b=st+b
        else:
            a=st+a
        carry =0
        i=len(a)-1
        ans=""
        while (i>=0):
            ans=str((int(a[i])+int(b[i])+carry)%2)+ans
            carry=(int (a[i])+int (b[i])+carry)//2
            i-=1
        if carry ==1 :
            ans='1'+ans
        return ans
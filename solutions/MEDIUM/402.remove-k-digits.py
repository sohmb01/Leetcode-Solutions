# Problem ID: 402
# Title: Remove K Digits
# Runtime: 49 ms

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        n = len(num)
        if n == 1:
            return "0"
        i=0
        while i<n:
            x = int(num[i])
            while k and st and st[-1] > x:
                st.pop()
                k-=1
            st.append(x)
            i+=1
        
        while k:
            st.pop()
            k-=1
        i = 0
        
        while i < len(st) and not st[i]  :
            i+=1
        res =  "".join([str(x) for x in st[i:]]) 
        return res if res else "0"
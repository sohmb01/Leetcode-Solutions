# Problem ID: 1818
# Title: Maximum Score From Removing Substrings
# Runtime: 233 ms

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        st = []
        points = 0
        target = "ab"
        if y>x:
            target = "ba"
        mxp,mnp = max(x,y),min(x,y)
        
        for c in s:
            if c in target:
                if st and st[-1] == target[0] and c == target[1]:
                    st.pop()
                    points+= mxp
                    continue
            st.append(c)
        
        st2 = []
        for c in st:
            if st2 and st2[-1] == target[1] and c==target[0]:
                st2.pop()
                points+=mnp
                continue
            st2.append(c)
                
        return points

            
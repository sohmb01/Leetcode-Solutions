# Problem ID: 2021
# Title: Remove All Occurrences of a Substring
# Runtime: 35 ms

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        st = []
        n = len(s)
        k = len(part)
        i = 0
        while i<n:
            st.append(s[i])
            length = len(st)
            if ''.join(st[-k:]) == part:
                st = st[:length-k]
            i+=1
        return ''.join(st)

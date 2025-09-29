# Problem ID: 3447
# Title: Clear Digits
# Runtime: 0 ms

class Solution:
    def clearDigits(self, s: str) -> str:
        st = []
        for char in s:
            if char.isdigit():
                st.pop()
            else:
                st.append(char)
        return ''.join(st)
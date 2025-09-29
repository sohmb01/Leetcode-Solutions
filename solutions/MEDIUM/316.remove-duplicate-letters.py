# Problem ID: 316
# Title: Remove Duplicate Letters
# Runtime: 9 ms

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt = Counter(s)
        st = []
        for ch in s:
            while st and ord(st[-1])>=ord(ch) and cnt[st[-1]]>1 and ch not in st:
                cnt[st.pop()]-=1
            if ch not in st:
                st.append(ch)
            else:
                cnt[ch]-=1
        return "".join(st)
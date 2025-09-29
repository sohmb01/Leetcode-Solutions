# Problem ID: 3445
# Title: Lexicographically Minimum String After Removing Stars
# Runtime: 499 ms

class Solution:
    def clearStars(self, s: str) -> str:
        res = list(s)
        st = []
        indices = [[] for _ in range(26)]
        for i, c in enumerate(s):
            if c != "*":
                indices[ord(c)-ord("a")].append(i)
            else:
                for i in range(26):
                    if indices[i]:
                        res[indices[i].pop()] = "*"
                        break
        return "".join(c for c in res if c!= "*")
        
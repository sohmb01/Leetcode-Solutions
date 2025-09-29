# Problem ID: 1915
# Title: Check if One String Swap Can Make Strings Equal
# Runtime: 0 ms

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        indices = []
        if len(s1)!=len(s2):
            return False
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                indices.append(i)
        if len(indices) == 0:
            return True
        if len(indices) != 2:
            return False
        return s1[indices[0]]==s2[indices[1]] and s1[indices[1]]==s2[indices[0]]


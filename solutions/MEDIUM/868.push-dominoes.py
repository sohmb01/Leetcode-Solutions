# Problem ID: 868
# Title: Push Dominoes
# Runtime: 279 ms

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        force = [0] * n
        f = 0
        for i in range(n):
            if dominoes[i] == "R": 
                f = n
            elif dominoes[i] == "L":
                f = 0
            else:
                f = max(f-1,0)
            force[i] += f
        f = 0
        for i in range(n-1,-1,-1):
            if dominoes[i] == "L":
                f = n
            elif dominoes[i] == "R":
                f = 0
            else:
                f = max(f-1,0)
            force[i] -= f
        res = ""
        for f in force:
            if f > 0:
                res+="R"
            elif f < 0:
                res+="L"
            else:
                res+="."
        return res
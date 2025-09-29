# Problem ID: 1058
# Title: Lexicographically Smallest Equivalent String
# Runtime: 4 ms

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        par = list(range(26))
        def find(a):
            if par[a] != a:
                return find(par[a])
            return par[a]
        
        def union(a,b):
            rootA,rootB = find(a),find(b)
            if rootA == rootB:
                return 
            elif rootA < rootB:
                par[rootB] = rootA
            else:
                par[rootA] = rootB
        
        for a,b in zip(s1,s2):
            union(ord(a)-ord('a'),ord(b)-ord('a'))
        res = []
        for c in baseStr:
            res.append(chr(find(ord(c)-ord('a'))+ord('a')))
        return "".join(res)

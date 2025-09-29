# Problem ID: 1516
# Title: The k-th Lexicographical String of All Happy Strings of Length n
# Runtime: 0 ms

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # [a,b,c]
        # [ab,ac,ba,bc,ca,cb]
        # ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]
        
        total = 3 * 2 ** (n-1)
        if k > total:
            return ""
        
        chars = "abc"
        res = []
        l,r = 1,total
        

        for i in range(n):
            partition = (r-l+1) // len(chars)
            curr = l
            for c in chars:
                if k in range(curr, curr+partition):
                    res.append(c)
                    l = curr
                    r = curr+partition-1
                    chars = "abc".replace(c,"")
                    break
                curr+= partition
        return "".join(res)
                


            

            
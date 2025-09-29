# Problem ID: 667
# Title: Beautiful Arrangement II
# Runtime: 0 ms

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = []
        if k == 1:
            return list(range(1,n+1))
        l,r = 1,k+1
        flag = True
        for i in range(k+1):
            if flag:
                res.append(l)
                l+=1
            else:
                res.append(r)
                r-=1
            flag = not flag
        for num in range(k+2,n+1):
            res.append(num)
        return res

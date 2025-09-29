# Problem ID: 414
# Title: Third Maximum Number
# Runtime: 0 ms

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        f,s,t=-999999999999999,-999999999999999,-999999999999999
        for i in nums:
            if i>f:
                s,t=f,s
                f=i
                continue
            if i>s and i!=f:
                s,t=i,s
                continue
            if i>t and i!=s and i!=f:
                t=i
        if t==-999999999999999:
            return f
        else:
            return t
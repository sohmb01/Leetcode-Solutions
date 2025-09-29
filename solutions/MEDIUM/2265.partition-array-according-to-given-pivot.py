# Problem ID: 2265
# Title: Partition Array According to Given Pivot
# Runtime: 56 ms

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l,r, m = 0,0,0
        for num in nums:
            if num == pivot:
                m+=1
            elif num<pivot:
                l+=1
            else:
                r+=1
        li, mi, ri = 0, l, l+m
        ret = [0] * len(nums)
        for num in nums:
            if num == pivot:
                ret[mi] = num
                mi+=1
            elif num<pivot:
                ret[li] = num
                li+=1
            else:
                ret[ri] = num
                ri+=1
        return ret
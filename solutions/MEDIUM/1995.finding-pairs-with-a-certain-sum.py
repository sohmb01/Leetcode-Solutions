# Problem ID: 1995
# Title: Finding Pairs With a Certain Sum
# Runtime: 217 ms

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.mp = {}
        self.nums1 = sorted(nums1)
        self.nums2 = nums2
        for num in nums2:
            if num not in self.mp:
                self.mp[num] = 1
            else:
                self.mp[num] += 1

    def add(self, index: int, val: int) -> None:
        ele = self.nums2[index]
        
        self.mp[ele] -= 1
        newVal = val + ele
        if newVal not in self.mp:
            self.mp[newVal] = 0
        self.mp[newVal] += 1
        self.nums2[index] = newVal

    

    def count(self, tot: int) -> int:
        res = 0
        for num in self.nums1:
            if tot < num:
                break
            if tot-num in self.mp:
                res+=self.mp[tot-num]
        return res


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
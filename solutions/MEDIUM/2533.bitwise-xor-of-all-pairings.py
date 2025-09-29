# Problem ID: 2533
# Title: Bitwise XOR of All Pairings
# Runtime: 13 ms

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        a,b = 0,0
        for num in nums1:
            a = a ^ num
        for num in nums2:
            b = b ^ num
        la, lb = len(nums1),len(nums2)
        if la % 2 and not lb % 2:
            ans = b
        elif not la % 2 and lb % 2:
            ans = a
        elif not la % 2 and not lb % 2:
            ans = 0
        else:
            ans = a^b
        return ans
# Problem ID: 55
# Title: Jump Game
# Runtime: 377 ms

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if length == 1:
            return True
        
        i = 0
        jumps_remaining = nums[i]+1
        while i < length:
            if jumps_remaining == 0:
                return False
            jumps_remaining -= 1
            jumps_remaining = max(nums[i],jumps_remaining)
            i+=1
        return True

# Problem ID: 42
# Title: Trapping Rain Water
# Runtime: 32 ms

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = [0]*n,[0]*n
        leftMax = height[0]
        rightMax = height[n-1]
        for i in range(1,n):
            leftMax = max(leftMax,height[i-1])
            left[i] = leftMax
        for i in range(n-2,-1,-1):
            rightMax = max(rightMax,height[i+1])
            right[i] = rightMax
        water = 0
        for i in range(n):
            water += max(0,min(left[i],right[i])-height[i])
        
        
        return water
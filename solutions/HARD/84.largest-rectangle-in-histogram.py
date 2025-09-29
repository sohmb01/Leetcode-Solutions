# Problem ID: 84
# Title: Largest Rectangle in Histogram
# Runtime: 183 ms

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = [(-1,0)]
        i = 1
        for i in range(len(heights)):
            start = i
            while stack[-1][0] != -1 and stack[-1][1] > heights[i]:
                x = stack.pop()
                ans = max(ans, (i-x[0])*x[1])
                start = x[0]
            stack.append((start,heights[i]))
            
        
        while stack[-1][0] != -1:
                x = stack.pop()
                ans = max(ans, (i-x[0]+1)*x[1])

        return ans

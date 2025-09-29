# Problem ID: 11
# Title: Container With Most Water
# Runtime: 1180 ms

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j  = 0, len(height)-1
        a = 0
        while i<j:
            low = min(height[i],height[j])
            high = max(height[i],height[j])
            temp = low * (j-i)
            a = max(temp,a)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
            print (str(low) + " " + str(high) + " " + str(a))
        return a
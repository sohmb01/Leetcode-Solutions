# Problem ID: 2316
# Title: Count Hills and Valleys in an Array
# Runtime: 0 ms

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        temp = []
        for num in nums:
            if temp and temp[-1]==num:
                continue
            temp.append(num)

        cnt = 0
        for i in range(1,len(temp)-1):
            if (temp[i]>temp[i-1] and temp[i]>temp[i+1]) or (temp[i]<temp[i-1] and temp[i]<temp[i+1]):
                cnt+=1
        return cnt
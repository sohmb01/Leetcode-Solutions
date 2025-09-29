# Problem ID: 456
# Title: 132 Pattern
# Runtime: 119 ms

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        st = [] # pair [val,minLeft] # Monotonically decreasing stack
        currMin = nums[0]
        for num in nums[1:]:
            while st and st[-1][0] <= num:
                st.pop()
            if st and st[-1][0] > num and num > st[-1][1]:
                return True
            currMin = min(currMin,num)
            st.append([num,currMin])
        return False
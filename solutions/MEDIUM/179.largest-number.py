# Problem ID: 179
# Title: Largest Number
# Runtime: 2 ms

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def compare(x,y):
            return -1 if x+y > y+x else 1
        nums = [str(num) for num in nums]
        nums.sort(key = cmp_to_key(compare))
        ans = "".join(nums)
        return '0' if ans[0] == '0' else ans
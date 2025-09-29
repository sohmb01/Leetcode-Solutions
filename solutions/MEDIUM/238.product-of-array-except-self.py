# Problem ID: 238
# Title: Product of Array Except Self
# Runtime: 250 ms

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = 0
        product = 1
        ans = []
        for num in nums:
            if num == 0:
                zeroes+=1
                continue
            product*= num
        if zeroes > 1:
            ans = [0]*len(nums)
        elif zeroes == 1:
            for num in nums:
                if num == 0:
                    ans.append(product)
                else:
                    ans.append(0)
        else:
            for num in nums:
                ans.append(product//num)
        return ans
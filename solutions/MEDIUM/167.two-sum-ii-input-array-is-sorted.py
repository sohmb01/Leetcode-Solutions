# Problem ID: 167
# Title: Two Sum II - Input Array Is Sorted
# Runtime: 11 ms

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1
        while l<r:
            mid = l + (r-l+1)//2
            if numbers[l]+numbers[r] == target:
                return [l+1,r+1]
            if numbers[l]+numbers[r] > target:
                r-=1
            if numbers[l]+numbers[r] < target:
                l+=1
        print("@")
        return [l,r+1]
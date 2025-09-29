# Problem ID: 2888
# Title: Minimum Index of a Valid Split
# Runtime: 103 ms

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        map1 = defaultdict(int)
        map2 = defaultdict(int)
        for num in nums:
            map1[num] +=1
        
        n = len(nums)
        for i in range(n):
            map2[nums[i]]+=1
            map1[nums[i]]-=1
            
            if map2[nums[i]] > (i+1)//2 and map1[nums[i]] > (n-i-1)//2:
                return i
        return -1

        
        
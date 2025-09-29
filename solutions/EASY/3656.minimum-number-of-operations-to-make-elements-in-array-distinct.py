# Problem ID: 3656
# Title: Minimum Number of Operations to Make Elements in Array Distinct
# Runtime: 0 ms

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        k = 0
        mp = defaultdict(int)
        for num in nums:
            mp[num]+=1
            if mp[num] == 2:
                k+=1
        if not k:
            return 0
        print(k)
        for i in range(n):
            num = nums[i]
            mp[num]-=1
            if mp[num] == 1:
                k-=1
            if not k:
                break
        print(i)
        res = (i+1)//3 
        if (i+1)%3:
            res+=1
        return res 



            
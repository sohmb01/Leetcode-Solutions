# Problem ID: 1364
# Title: Tuple with Same Product
# Runtime: 362 ms

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        cnt = 0
        n = len(nums)
        mp = defaultdict(int)
        for i in range(n):
            for j in range(i+1,n):
                mp[nums[i]*nums[j]] += 1

        for k,val in mp.items():
            if val>1:
                cnt +=  (val * (val-1))//2

        return cnt*8
# Problem ID: 3332
# Title: Minimum Operations to Exceed Threshold Value II
# Runtime: 215 ms

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap,num)
        n = len(nums)-1
        cnt = 0
        while n:  
            a = heappop(heap)
            if a >= k:
                break
            b = heappop(heap)
            temp = (a*2) + b
            heappush(heap,temp)
            cnt+=1
            n-=1
        return cnt

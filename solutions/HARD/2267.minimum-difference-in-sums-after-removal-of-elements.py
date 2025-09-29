# Problem ID: 2267
# Title: Minimum Difference in Sums After Removal of Elements
# Runtime: 394 ms

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        N = len(nums)
        n = N//3
        p1 = [0] * (N+1)
        total = sum(nums[:n])
        maxHeap = [-x for x in nums[:n]]
        heapify(maxHeap)
        p1[0] = total
        for i in range(n,n*2):
            total += nums[i]
            heappush(maxHeap, -nums[i])
            total -= -heappop(maxHeap)
            p1[i - (n-1)] = total
        
        total = sum(nums[2*n:])
        minHeap = nums[n*2:]
        heapify(minHeap)
        ans = p1[n] - total

        for i in range(n*2-1,n-1,-1):
            total += nums[i]
            heappush(minHeap,nums[i])
            total -= heappop(minHeap)
            ans = min(ans,p1[i-n]-total)
        
        return ans
        
# Problem ID: 239
# Title: Sliding Window Maximum
# Runtime: 118 ms

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()

        #initialize window
        for i in range(k):
            while q and q[-1]<nums[i]:
                q.pop()
            q.append(nums[i])
        
        ans = [q[0]]
        for i in range(k,len(nums)):
            if nums[i-k] == q[0]:
                q.popleft()
            while q and q[-1]<nums[i]:
                q.pop()
            q.append(nums[i])
            ans.append(q[0])
        return ans
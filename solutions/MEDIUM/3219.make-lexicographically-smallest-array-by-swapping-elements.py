# Problem ID: 3219
# Title: Make Lexicographically Smallest Array by Swapping Elements
# Runtime: 220 ms

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        
        n = len(nums)
        queues = []
        last = -float('inf')
        mp = {}
        for num in sorted(nums):
            if num - last > limit:
                q = deque([num])
                queues.append(q)
            else:
                queues[-1].append(num)

            mp[num] = len(queues) - 1
            last = num
        ans = []
        for num in nums:
            ans.append(queues[mp[num]].popleft())
        return ans
                

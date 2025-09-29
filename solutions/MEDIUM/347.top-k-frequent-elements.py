# Problem ID: 347
# Title: Top K Frequent Elements
# Runtime: 91 ms

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums)
        ans = []
        mp = dict(sorted(mp.items(), key = lambda item: item[1], reverse = True))
        return list(mp.keys())[:k]
        
        
        
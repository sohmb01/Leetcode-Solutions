# Problem ID: 2915
# Title: Count of Interesting Subarrays
# Runtime: 187 ms

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        res = acc = 0
        cnt = Counter({0:1})
        for num in nums:
            acc = (acc + (1 if num % modulo == k else 0))%modulo
            res += (cnt[(acc - k)%modulo])
            cnt[acc] += 1
        return res
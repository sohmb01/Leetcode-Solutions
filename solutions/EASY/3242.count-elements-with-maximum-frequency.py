# Problem ID: 3242
# Title: Count Elements With Maximum Frequency
# Runtime: 0 ms

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        maxFreq = max(c.values())
        n = 0
        for k,v in c.items():
            if v == maxFreq:
                n+=1
        return n*maxFreq
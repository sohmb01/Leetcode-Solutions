# Problem ID: 3143
# Title: Longest Unequal Adjacent Groups Subsequence I
# Runtime: 0 ms

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        curr = -1
        for idx,group in enumerate(groups):
            if group != curr:
                curr = group
                res.append(words[idx])
        return res

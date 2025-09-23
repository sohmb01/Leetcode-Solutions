/**
 * Leetcode Solution for: 4. Median of Two Sorted Arrays
 * Difficulty: Hard
 * URL: https://leetcode.com/problems/median-of-two-sorted-arrays/
 * Submitted: 2025-09-23T18:35:37.737Z
 */

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        f,s,t=-999999999999999,-999999999999999,-999999999999999
        for i in nums:
            if i>f:
                s,t=f,s
                f=i
                continue
            if i>s and i!=f:
                s,t=i,s
                continue
            if i>t and i!=s and i!=f:
                t=i
        if t==-999999999999999:
            return f
        else:
            return t
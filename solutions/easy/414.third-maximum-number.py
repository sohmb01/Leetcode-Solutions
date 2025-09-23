/**
 * Leetcode Solution for: 414. Third Maximum Number
 * Difficulty: Easy
 * URL: https://leetcode.com/problems/third-maximum-number/description/
 * Submitted: 2025-09-23T20:03:10.781Z
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
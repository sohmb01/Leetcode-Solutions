/**
 * Leetcode Solution for: 374. Guess Number Higher or Lower
 * Difficulty: Easy
 * URL: https://leetcode.com/problems/guess-number-higher-or-lower/description/
 * Submitted: 2025-09-23T18:47:54.571Z
 */

# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n):
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1
        
# @param num, your guess
# The guess API is already defined for you.
/**
 * Leetcode Solution for: 605. Can Place Flowers
 * Difficulty: Easy
 * URL: https://leetcode.com/problems/can-place-flowers/submissions/1780572625/
 * Submitted: 2025-09-23T19:27:47.602Z
 */

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            left = i == 0 or flowerbed[i-1] == 0
            right = i == len(flowerbed) - 1 or flowerbed[i+1] == 0

            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        
        return n <= 0
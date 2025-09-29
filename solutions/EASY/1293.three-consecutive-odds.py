# Problem ID: 1293
# Title: Three Consecutive Odds
# Runtime: 0 ms

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        product = arr[0] * arr[1] * arr[2]
        if product % 2 == 1:
            return True
        for i in range(3,len(arr)):
            product //= arr[i-3]
            product *= arr[i]
            if product % 2 == 1:
                return True
        return False
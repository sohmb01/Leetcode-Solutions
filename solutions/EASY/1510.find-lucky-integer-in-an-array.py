# Problem ID: 1510
# Title: Find Lucky Integer in an Array
# Runtime: 3 ms

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        ans = -1
        for num in arr:
            if c[num] == num:
                ans = max(num,ans)
        return ans
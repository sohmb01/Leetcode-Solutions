# Problem ID: 934
# Title: Bitwise ORs of Subarrays
# Runtime: 454 ms

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        curr = {0}
        for num in arr:
            curr = { num | x for x in curr} | {num}
            ans |=curr
        return len(ans)
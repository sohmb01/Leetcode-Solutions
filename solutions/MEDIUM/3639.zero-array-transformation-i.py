# Problem ID: 3639
# Title: Zero Array Transformation I
# Runtime: 73 ms

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0]* (n+1)

        for l,r in queries:
            diff[l] += 1
            diff[r+1] -= 1

        cum = 0
        operations = []

        for d in diff:
            cum += d
            operations.append(cum)

        for operation, target in zip(operations, nums):
            if operation < target:
                return False
        return True

# Problem ID: 437
# Title: Path Sum III
# Runtime: 9 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, currSum):
            if not node:
                return 0
            currSum+=node.val
            count = sums[currSum-targetSum]
            sums[currSum]+=1
            count+=dfs(node.left, currSum) + dfs(node.right,currSum)
            sums[currSum]-=1
            return count

        sums = defaultdict(int)
        sums[0] = 1
        return dfs(root,0)
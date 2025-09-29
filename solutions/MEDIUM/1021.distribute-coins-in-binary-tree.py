# Problem ID: 1021
# Title: Distribute Coins in Binary Tree
# Runtime: 4 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(curr):
            if not curr:
                return 0
            l = dfs(curr.left)
            r = dfs(curr.right)
            self.moves += abs(l) + abs(r)

            return curr.val - 1 + l + r
        dfs(root)
        return self.moves
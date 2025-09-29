# Problem ID: 110
# Title: Balanced Binary Tree
# Runtime: 3 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # returns height diff
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)

            if l<0 or r<0 or abs(l-r) > 1:
                return -1
            return max(l,r)+1

        return dfs(root) >= 0

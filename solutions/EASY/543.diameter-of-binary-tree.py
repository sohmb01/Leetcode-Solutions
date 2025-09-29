# Problem ID: 543
# Title: Diameter of Binary Tree
# Runtime: 3 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node):
            if not node:
                return 0
            nonlocal ans
            l = dfs(node.left)
            r = dfs(node.right)
            ans = max(ans,l+r)
            return 1+max(l,r)
        dfs(root)
        return ans


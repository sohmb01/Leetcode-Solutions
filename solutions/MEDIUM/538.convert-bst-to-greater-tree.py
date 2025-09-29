# Problem ID: 538
# Title: Convert BST to Greater Tree
# Runtime: 4 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.s = 0
        def dfs(node):
            if not node:
                return

            if node.right:
                dfs(node.right)
            node.val+= self.s
            self.s = node.val
            if node.left:
                dfs(node.left)
        dfs(root)
        return root
            
            
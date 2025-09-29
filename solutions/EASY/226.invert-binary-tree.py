# Problem ID: 226
# Title: Invert Binary Tree
# Runtime: 24 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.invert(root)
        return root
    def invert(self,root):
        if root:
            root.left,root.right=root.right,root.left
            self.invert(root.left)
            self.invert(root.right)
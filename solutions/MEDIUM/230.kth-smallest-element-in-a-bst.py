# Problem ID: 230
# Title: Kth Smallest Element in a BST
# Runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = []
        def inorder(node):
            if not node:
                return
            if node.left:
                inorder(node.left)
            l.append(node.val)
            if node.right:
                inorder(node.right)
        inorder(root)
        return l[k-1]
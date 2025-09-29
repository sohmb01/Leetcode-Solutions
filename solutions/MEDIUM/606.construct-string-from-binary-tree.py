# Problem ID: 606
# Title: Construct String from Binary Tree
# Runtime: 4 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        s = ""
        if not root:
            return s
        temp = str(root.val)
        left = self.tree2str(root.left)
        if left:
            left = "(" + left +")"
        right = self.tree2str(root.right)
        if right:
            right = "(" + right +")"
        if right and not left:
            left = "()"

        return temp + left + right
        

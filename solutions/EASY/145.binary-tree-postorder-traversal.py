# Problem ID: 145
# Title: Binary Tree Postorder Traversal
# Runtime: 32 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        l=[]
        self.helper(root,l)
        return l
    def helper(self, node, l):
        if node:
            self.helper(node.left,l)
            self.helper(node.right,l)
            l.append(node.val)
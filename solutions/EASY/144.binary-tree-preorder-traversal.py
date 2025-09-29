# Problem ID: 144
# Title: Binary Tree Preorder Traversal
# Runtime: 32 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        l=[]
        self.helper(root , l)
        return l
        
    def helper (self,node,l):
        if node:
            l.append(node.val)
            self.helper(node.left,l)
            self.helper(node.right,l)
            
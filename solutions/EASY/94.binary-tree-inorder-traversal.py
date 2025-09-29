# Problem ID: 94
# Title: Binary Tree Inorder Traversal
# Runtime: 32 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        l=[]
        self.helper(root,l)
        return l
    def helper(self,node,l):
        if node:
            if node.left:
                self.helper(node.left,l)
            l.append(node.val)
            if node.right:
                self.helper(node.right,l)
    
        
        
        
            
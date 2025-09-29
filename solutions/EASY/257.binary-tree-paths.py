# Problem ID: 257
# Title: Binary Tree Paths
# Runtime: 32 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root :
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        l= [str(root.val) + '->' + i for i in self.binaryTreePaths(root.left)] +[str(root.val) + '->' + i for i in self.binaryTreePaths(root.right)] 
        
        return l
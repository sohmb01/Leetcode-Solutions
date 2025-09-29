# Problem ID: 1218
# Title: Lowest Common Ancestor of Deepest Leaves
# Runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node): # returns (node, height)
            if not node:
                return None, 0
            
            leftNode, leftHeight = dfs(node.left)
            rightNode, rightHeight = dfs(node.right)

            if leftHeight == rightHeight:
                return node, 1+leftHeight
            elif leftHeight > rightHeight:
                return leftNode, 1+leftHeight
            else:
                return rightNode, 1+rightHeight
        
        node,_ = dfs(root)
        return node
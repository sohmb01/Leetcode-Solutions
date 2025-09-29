# Problem ID: 112
# Title: Path Sum
# Runtime: 32 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def PathSum(node,val):
            if not node:
                return False
            val-=node.val
            if val==0 and not node.left and not node.right:
                return True
            
            return PathSum(node.left,val) or PathSum(node.right,val)
        return PathSum(root,sum)
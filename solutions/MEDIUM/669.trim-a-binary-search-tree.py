# Problem ID: 669
# Title: Trim a Binary Search Tree
# Runtime: 44 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def trim(root,low,high):
        if not root:
            return None
        elif root.val<low:
            return trim(root.right,low,high)
        elif root.val>high:
            return trim(root.left,low,high)
        else:
            root.left=trim(root.left,low,high)
            root.right=trim(root.right,low,high)
        return root
class Solution:
    
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        return trim(root,low,high)
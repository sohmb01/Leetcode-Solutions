# Problem ID: 101
# Title: Symmetric Tree
# Runtime: 32 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return isMirror(root,root)
    
def isMirror(a:TreeNode,b:TreeNode):
    if a==None and b==None:
        return True
    if a is not None and b is not None:
        return (a.val==b.val) and (isMirror(a.left,b.right)) and (isMirror(a.right,b.left))
    return False
# Problem ID: 572
# Title: Subtree of Another Tree
# Runtime: 73 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self,p,q):
        if p==None or q==None:
            if p == None and q ==None:
                return True
            else:
                return False
        return (p.val == q.val) and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root ==None or subRoot==None:
            if root == None and subRoot ==None:
                return True
            else:
                return False

        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
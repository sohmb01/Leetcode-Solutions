# Problem ID: 450
# Title: Delete Node in a BST
# Runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(prev, curr, val):
            if not curr:
                return None, None
            if curr.val == val:
                return prev, curr
            elif curr.val > val:
                return dfs(curr, curr.left,val)
            else:
                return dfs(curr, curr.right,val)
        
        def mergeTrees(a, b):
            if not a: return b
            if not b: return a
            curr = a
            while curr and curr.right:
                curr = curr.right
            curr.right = b
            return a
                
        par, node = dfs(None, root, key)
        if not node:
            return root
        
        # we need to delete node from the tree
        subTree = mergeTrees(node.left, node.right)
        if not par:
            return subTree
        if par and par.val > node.val:
            par.left = subTree
        else:
            par.right = subTree
        if not subTree:
            return root
        
        return root


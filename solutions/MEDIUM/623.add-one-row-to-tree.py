# Problem ID: 623
# Title: Add One Row to Tree
# Runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            root = TreeNode(val,root,None)
            return root
        def dfs(node,currDepth):
            if not node:
                return 

            if currDepth == depth-1:
                node.left = TreeNode(val, node.left, None)
                node.right = TreeNode(val,None, node.right)
                return
            
            dfs(node.left,currDepth+1)
            dfs(node.right,currDepth+1)
        
        dfs(root,1)
        return root

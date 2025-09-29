# Problem ID: 1544
# Title: Count Good Nodes in Binary Tree
# Runtime: 131 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node,val):
            if not node:
                return 
            nonlocal ans
            if node.val>=val:
                ans+=1
            dfs(node.left,max(node.val,val))
            dfs(node.right,max(node.val,val))

        dfs(root,root.val)
        return ans
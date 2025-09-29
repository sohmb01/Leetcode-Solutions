# Problem ID: 124
# Title: Binary Tree Maximum Path Sum
# Runtime: 19 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val
        def bfs(node):
            if node == None:
                return 0
            l = max(0,bfs(node.left))
            r = max(0,bfs(node.right))
            nonlocal ans
            ans = max(ans, node.val + l + r)
            return node.val + max(l,r)
        bfs(root)
        return ans
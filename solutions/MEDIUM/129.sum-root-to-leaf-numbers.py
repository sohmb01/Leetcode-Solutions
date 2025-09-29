# Problem ID: 129
# Title: Sum Root to Leaf Numbers
# Runtime: 0 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s = []
        def dfs(curr, num):
            if not curr:
                return
            num = num*10 + curr.val
            if not curr.left and not curr.right:
                s.append(num)
            dfs(curr.left,num)
            dfs(curr.right,num)
        dfs(root,0)
        return sum(s)
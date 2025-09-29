# Problem ID: 513
# Title: Find Bottom Left Tree Value
# Runtime: 4 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = [-1]
        def dfs(level):
            if not level:
                return
            ans[0] = level[0].val
            temp = []
            for node in level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            dfs(temp)
        dfs([root])
        return ans[0]
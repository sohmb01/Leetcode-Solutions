# Problem ID: 102
# Title: Binary Tree Level Order Traversal
# Runtime: 3 ms

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return []
        def helper(level):
            temp = []
            for node in level:
                temp.append(node)
            return temp
        l = [root]
        while l:
            ans.append([x.val for x in l])
            level = helper(l)
            l = []
            for node in level:
                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)
        return ans